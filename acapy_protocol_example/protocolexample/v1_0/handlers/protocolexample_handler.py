from aries_cloudagent.messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext,
)

from ..messages.protocolexample import ProtocolExample
from ..messages.protocolexample_response import ProtocolExampleResponse

class ProtocolExampleHandler(BaseHandler):

    async def handle(self, context: RequestContext, responder: BaseResponder):

        self._logger.debug(f"ProtocolExampleHandler called with context {context}")
        assert isinstance(context.message, ProtocolExample)

        self._logger.info(
            "Received protocolexample message from: %s", context.message_receipt.sender_did
        )

        if not context.connection_ready:
            self._logger.info(
                "Connection not active, skipping protocolexample response: %s",
                context.message_receipt.sender_did,
            )
            return

        if context.message.response_requested:
            reply = ProtocolExampleResponse()
            reply.assign_thread_from(context.message)
            reply.assign_trace_from(context.message)
            await responder.send_reply(reply)



        if context.settings.get("debug.monitor_protocolexample"):
            await responder.send_webhook(
                "protocolexample",
                {
                    "example": context.message.example,
                    "connection_id": context.message_receipt.connection_id,
                    "state": "received",
                    "thread_id": context.message._thread_id,
                },
            )
