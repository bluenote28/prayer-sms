from aws_cdk import Stack
from aws_cdk.aws_dynamodb import Table, Attribute, AttributeType
import aws_cdk.aws_signer as signer
from aws_cdk.aws_lambda import Function, CodeSigningConfig, Runtime, Code
import os
from constructs import Construct

class PrayerSmsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        prayertable = Table(self, "PrayerIntentionTable",
                        partition_key=Attribute(
                                        name="intention",
                                        type=AttributeType.STRING)
        )

        ##lambda
        signing_profile = signer.SigningProfile(self, "SigningProfile",
        platform=signer.Platform.AWS_LAMBDA_SHA384_ECDSA)

        code_signing_config = CodeSigningConfig(self, "CodeSigningConfig",
        signing_profiles=[signing_profile])

        Function(self, "Function",
        code_signing_config=code_signing_config,
        runtime=Runtime.PYTHON_3_12,
        handler="prayer_handler.handler",
        code=Code.from_asset(os.path.join(os.path.dirname('prayer_sms'), "prayer-handler")))
