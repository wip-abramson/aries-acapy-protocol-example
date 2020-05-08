
from marshmallow import fields

from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema

from ..message_types import PROTOCOL_EXAMPLE_RESPONSE, PROTOCOL_PACKAGE


HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.protocolexample_response_handler.ProtocolExampleResponseHandler"


class ProtocolExampleResponse(AgentMessage):

    class Meta:

        handler_class = HANDLER_CLASS
        message_type = PROTOCOL_EXAMPLE_RESPONSE
        schema_class = "ProtocolExampleResponseSchema"

    def __init__(self, *, example: str, **kwargs):

        super(ProtocolExampleResponse, self).__init__(kwargs)
        self.example = example


class ProtocolExampleResponseSchema(AgentMessageSchema):

    class Meta:

        model_class = ProtocolExampleResponse

    example = fields.Str(
        required=False,
        description="This is an example of a string field in your message",
        example="this is an example",
        allow_none=False
    )

