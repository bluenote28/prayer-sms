import aws_cdk as core
import aws_cdk.assertions as assertions

from prayer_sms.prayer_sms_stack import PrayerSmsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in prayer_sms/prayer_sms_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PrayerSmsStack(app, "prayer-sms")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
