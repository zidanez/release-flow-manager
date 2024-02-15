import typing as t

from adapters import BaseAdapter
from resources import BaseResoure



class ChildBase:
    class Story(BaseResoure):
        pass


    class Task(BaseResoure):
        pass


class BaseRelease(BaseResoure):

    def __init__(self, adapter: BaseAdapter = None, task_list: t.List[str] = None) -> None:
        super().__init__(adapter)
        self._child_resources: t.List[BaseResoure] = []
        self._task_list = task_list



        for task in task_list:
            resource_info: dict = self.adapter.get_resource(task)

            child_klass = getattr(ChildBase, str(resource_info["type"]).capitalize())
            if resource_info:
                resource: ChildBase.Task = child_klass(fields=resource_info)
            else:
                resource = child_klass()
            
            self._child_resources.append(resource)


def main(task_list: t.List[str]):
    release = BaseRelease(task_list=task_list)
    # release.change_state("prom")
    print(release._child_resources)

    BaseResoure
    for chilld in release._child_resources:
        print(chilld.FIELDS.start_date)
    

if __name__ == '__main__':
    main(task_list=["TASK", "STORY"])

