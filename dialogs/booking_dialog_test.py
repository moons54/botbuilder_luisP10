import sys
import pathlib
import pytest
import aiounittest
import asyncio

from botbuilder.dialogs.prompts import (
    AttachmentPrompt, 
    PromptOptions, 
    PromptValidatorContext,
    text_prompt, 
)

from botbuilder.core import (
    TurnContext, 
    ConversationState, 
    MemoryStorage, 
    MessageFactory, 
)
from botbuilder.schema import Activity, ActivityTypes, Attachment
from botbuilder.dialogs import DialogSet, DialogTurnStatus, TextPrompt
from botbuilder.core.adapters import TestAdapter
from booking_dialog import BookingDialog



class BookingDialogTest(aiounittest.AsyncTestCase):
   async def test_booking_dialog(self):
       # Create adapter.
       adapter = TestAdapter()
       # Create empty memory storage.
       memory_storage = MemoryStorage()
       # Create conversation state with memory storage.
       conversation_state = ConversationState(memory_storage)
       # Create dialog state property.
       dialog_state = conversation_state.create_property("dialog_state")
       # Create dialog set.
       dialogs = DialogSet(dialog_state)
       # Create and add text prompt.
       text_prompt = TextPrompt(name="text")
       dialogs.add(text_prompt)
       # Create and add booking dialog.
       booking_dialog = BookingDialog(name="booking")
       dialogs.add(booking_dialog)
       # Listen for incoming requests.
       async def on_turn(turn_context: TurnContext):
           # Create dialog context.
           dialog_context = await dialogs.create_context(turn_context)
           # Continue current dialog.
           results = await dialog_context.continue_dialog()
           # If no one has responded,
           if results.status == DialogTurnStatus.empty:
               # Start booking dialog.
               await dialog_context.begin_dialog("booking")
           elif results.status == DialogTurnStatus.complete:
               # Print out booking details.
               print(results.result)
       # Listen for incoming requests.
       await adapter.process_activity(on_turn)
