"""Ping response handler."""

from aries_cloudagent.messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext,
)

from ..messages.protocolexample_response import ProtocolExampleResponse


class ProtocolExampleResponseHandler(BaseHandler):
    """Protocol Example response handler class."""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """
        Handle protocolexample response message.

        Args:
            context: Request context
            responder: Responder used to reply

        """

        self._logger.debug("ProtocolExampleResponseHandler called with context: %s", context)
        assert isinstance(context.message, ProtocolExampleResponse)

        self._logger.info(
            "Received trust protocolexample response from: %s", context.message_receipt.sender_did
        )

        if context.settings.get("debug.monitor_protocolexample"):
            await responder.send_webhook(
                "ping",
                {
                    "comment": context.message.comment,
                    "connection_id": context.message_receipt.connection_id,
                    "state": "response_received",
                    "thread_id": context.message._thread_id,
                },
            )

        # Nothing to do, Connection should be automatically promoted to 'active'
