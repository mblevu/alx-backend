const kue = require('kue');

// Create a new queue
const queue = kue.createQueue();

// Define the job data
const jobData = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
}

// create push_notification_code queue
const job = queue.create('push_notification_code', jobData).save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
});

// If the job is completed, log to the console
job.on('complete', () => {
    console.log('Notification job completed');
});

// If the job is failed, log to the console
job.on('failed', () => {
    console.log('Notification job failed');
});
