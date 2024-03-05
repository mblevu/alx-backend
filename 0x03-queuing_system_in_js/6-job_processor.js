const kue = require('kue');

// Create a new queue
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Process the queue
queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
    console.log('Notification job completed');
});
