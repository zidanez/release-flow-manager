import typing as t


class BaseAdapter:
    def __init__(self):
        pass

    def create_resource(self):
        pass

    def get_resource(self, id_resource: str):
        if id_resource == "TASK":
            return {"type": "task", "field_name": "TEST_TASK", "customfield_132": "00:00:00", "test": "qwerty"}
        return {"type": "task"}


    def get_all_states(self) -> t.List:
        return ["dev", "ift", "psi", "prom"]

    def get_current_state(self):
        pass

    def create_link(self):
        pass

    def get_transitions(self, id_resource: str):
        pass

    def set_transition(self, id_resource: str):
        pass
