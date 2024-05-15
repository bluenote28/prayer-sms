#!/usr/bin/env python3
import os

import aws_cdk as cdk

from prayer_sms.prayer_sms_stack import PrayerSmsStack


app = cdk.App()
PrayerSmsStack(app, "PrayerSmsStack",
    

    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))
    )

app.synth()
