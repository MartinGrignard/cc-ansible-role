"""Post project generation hook."""
from functools import partial
import subprocess
from typing import Callable

from rich import print
from rich.text import Text


class Step:
    """A step of the hook."""
    n_steps : int = 0

    def __init__(self, message: str, func: Callable) -> None:
        Step.n_steps += 1
        self._index = Step.n_steps
        self._message = message
        self._func = func
    
    def __call__(self, *args, **kwargs) -> None:
        """Run the step after printing its message."""
        self.print_message()
        self._func(*args, **kwargs)
    
    @property
    def index(self) -> int:
        """Return the index of the step."""
        return self._index

    @property
    def message(self) -> str:
        """Return the message of the step."""
        return self._message
    
    def print_message(self) -> None:
        """Print the message of the step."""
        print(
            Text(f"  [{self.index}/{Step.n_steps}]", style="#727272"),
            Text(self.message)
        )
    

def step(message: str):
    """Convert a function into a Step object."""
    def decorator(func: Callable):
        return Step(message, func)
    return decorator

run = partial(subprocess.run, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


@step("Initializing Git repository...")
def init_git_repository() -> None:
    """Initialise the Git repository."""
    try:
        run(["git", "--version"])
    except Exception:
        print(Text("\t[error]", style="red"), Text("Command 'git' not found."))
    run(["git", "init", "."])
    run(["git", "checkout", "-b", "main"])
    github_repository = "{{ cookiecutter.role_repository }}"
    if github_repository:
        run(["git", "remote", "add", "origin", github_repository])


if __name__ == "__main__":
    print(Text("Post project generation hook", style="bold green"))
    init_git_repository()
