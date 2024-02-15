from typing import Any
import uuid

import typing as t

from transitions import Machine
from adapters import BaseAdapter

class FieldValue:
    pass

class BaseFields(object):

    name = "field_name"
    type = "type"
    start_date = "customfield_132"
    end_date = "customfield_132"

    def __get__(self, instance, owner):
        called_klass = instance

        try:
            source_fields: dict = getattr(called_klass, "_fields")
        except AttributeError:
            raise AttributeError(f"Not set attribute _fields in {called_klass.__class__.__name__} class")

        obj = FieldValue()

        for key in dir(self):
            if key[:1] == '_':
                continue

            val = getattr(self, key)
            source_value = source_fields.get(str(val), "")
            setattr(obj, key, source_value)
        return obj

class BaseResoure(object):

    FIELDS = BaseFields()

    @property
    def adapter(self):
        return self._adapter

    @property
    def states(self):
        return self._states
    

    def __init__(self, adapter: BaseAdapter = None, fields: dict = None) -> None:
        self._adapter = adapter if adapter else BaseAdapter()
        self._fields = fields

        self._states: t.List = self._adapter.get_all_states()
        self._current_state = self._adapter.get_current_state()

        self.st_machine: Machine = Machine(states=self._states, initial=self._states[0])

        for state in self.states:
            if state == self.states[0]:
                prev_state = state
                continue
            self.st_machine.add_transition(trigger=f'move_{state}', source=prev_state, dest=state)
            prev_state = state

    def change_state(self, state_name: str):
        method = self.st_machine.__getattr__(f'move_{state_name}')
        method()
        print(self.st_machine.state)
