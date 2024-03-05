const kue = require('kue');

const queue = kue.createQueue({
    concurrency: 2
});

const blacklistedPhoneNumbers = [4153518780, 4153518781];

function sendNotification(phoneNumber, message, job, done) {
    if (blacklistedPhoneNumbers.includes(phoneNumber)) {
        return done(Error(`Phone number ${phoneNumber} is blacklisted`));
    } else {
        progress(job, 0, 100);
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
        progress(job, 50, 100);
        done();
    }
}
