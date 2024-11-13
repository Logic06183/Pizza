// Utility functions for the pizza management system
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // Add animation to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseover', function() {
            this.style.transform = 'translateY(-5px)';
        });
        card.addEventListener('mouseout', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Status update handler
    const statusSelects = document.querySelectorAll('.status-select');
    statusSelects.forEach(select => {
        select.addEventListener('change', function(e) {
            const orderId = this.dataset.orderId;
            updateOrderStatus(orderId, this.value);
        });
    });

    // Time update function
    function updateTime() {
        const timeDisplay = document.querySelector('.current-time');
        if (timeDisplay) {
            const now = new Date();
            timeDisplay.textContent = now.toLocaleTimeString();
        }
    }
    setInterval(updateTime, 1000);

    // Form validation
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Initialize time display and order timers
    updateTimeDisplay();
    updateOrderTimers();

    // Set up intervals for updating time and timers
    setInterval(updateTimeDisplay, 1000);
    setInterval(updateOrderTimers, 1000);
});

// Async function to update order status
async function updateOrderStatus(orderId, status) {
    try {
        const response = await fetch(`/api/orders/${orderId}/status/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ status: status })
        });
        
        if (!response.ok) throw new Error('Network response was not ok');
        
        // Show success message
        showNotification('Status updated successfully!', 'success');
    } catch (error) {
        console.error('Error:', error);
        showNotification('Failed to update status', 'error');
    }
}

// Utility function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Notification function
function showNotification(message, type) {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} notification`;
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Update time remaining for each order
function updateTimeRemaining() {
    const rows = document.querySelectorAll('.order-row');
    const now = new Date();

    rows.forEach(row => {
        const dueTime = new Date(row.dataset.dueTime);
        const timeLeft = dueTime - now;
        const countdown = row.querySelector('.countdown');
        
        const minutes = Math.floor(timeLeft / 60000);
        const seconds = Math.floor((timeLeft % 60000) / 1000);
        
        // Update countdown display
        countdown.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
        
        // Update row status based on time remaining
        row.classList.remove('status-normal', 'status-warning', 'status-urgent');
        
        if (timeLeft < 0) {
            countdown.textContent = 'LATE!';
            countdown.style.color = 'var(--danger-color)';
            row.classList.add('status-urgent');
        } else if (minutes < 5) {
            countdown.style.color = 'var(--warning-color)';
            row.classList.add('status-warning');
        } else {
            countdown.style.color = 'var(--success-color)';
            row.classList.add('status-normal');
        }
    });
}

// Start timer updates with shorter interval for smoother countdown
setInterval(updateTimeRemaining, 500);

// Handle order status updates
async function updateOrderStatus(orderId, newStatus) {
    try {
        const response = await fetch(`/api/orders/${orderId}/status/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ status: newStatus })
        });

        if (!response.ok) throw new Error('Network response was not ok');
        const data = await response.json();

        if (newStatus === 'completed') {
            const row = document.querySelector(`[data-order-id="${orderId}"]`);
            row.classList.add('fade-out');
            
            // Move to completed orders if the container exists
            const completedContainer = document.querySelector('.completed-orders tbody');
            if (completedContainer) {
                // Clone and modify row for completed orders
                const completedRow = row.cloneNode(true);
                completedRow.classList.remove('fade-out');
                // Remove action buttons and countdown
                completedRow.querySelector('.action-buttons').remove();
                completedRow.querySelector('.countdown').textContent = 'Completed';
                
                // Add to completed orders
                completedContainer.insertBefore(completedRow, completedContainer.firstChild);
            }
            
            // Remove from active orders
            setTimeout(() => row.remove(), 500);
        }

        showNotification('Order updated successfully!', 'success');
    } catch (error) {
        console.error('Error:', error);
        showNotification('Failed to update order', 'error');
    }
}

// Update the current time display
function updateTimeDisplay() {
    const timeDisplay = document.getElementById('current-time');
    if (timeDisplay) {
        timeDisplay.textContent = new Date().toLocaleTimeString();
    }
}

// Update timers and statuses for orders
function updateOrderTimers() {
    const rows = document.querySelectorAll('#active-orders-body .order-row');
    const now = new Date();

    rows.forEach(row => {
        const dueTime = new Date(row.dataset.dueTime);
        const timeLeft = dueTime - now;
        const countdown = row.querySelector('.countdown');

        if (!countdown) return;

        // Remove existing status classes
        row.classList.remove('status-normal', 'status-warning', 'status-urgent');

        if (timeLeft < 0) {
            // Order is overdue
            countdown.textContent = 'LATE!';
            countdown.style.color = '#f44336';
            row.classList.add('status-urgent');
        } else {
            // Calculate minutes and seconds left
            const minutes = Math.floor(timeLeft / 60000);
            const seconds = Math.floor((timeLeft % 60000) / 1000);
            countdown.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;

            if (minutes < 5) {
                countdown.style.color = '#ff9800';
                row.classList.add('status-warning');
            } else {
                countdown.style.color = '#4caf50';
                row.classList.add('status-normal');
            }
        }
    });
}
