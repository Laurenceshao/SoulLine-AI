from tasks.task import BaseTask
from typing import Any, List, Dict


class AskUser(BaseTask):
  name: str = "ask_user"
  chat_name: str = "AskUser"
  description: str = (
      "Ask user to provide more information or directly answer user's question. You should try your best using other tools before calling this tool."      
  )
  dependencies: List[str] = []
  inputs: List[str] = ["The text returned to user. It should be relevant and very detailed based on the latest user's Question."]
  outputs: List[str] = []
  output_type: bool = False
  return_direct: bool = True

  translator: Any = None  #: :meta private:

  def _execute(
    self,
    inputs: List[Any],
  ) -> str:
    """Translate query"""
    return inputs[0]

  def explain(
        self,
      ) -> str:
    return (
      "This task simply asks user to provide more information or continue interaction."
    )