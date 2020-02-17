from typing import Any, Callable, Dict, List
from .types import Example


class Dataset:
    """Container for a full dataset with train/dev/test splits.
    Used to apply core functions to all datasets at once.
    """
    
    def __init__(self,
                 train: List[Example],
                 dev: List[Example],
                 test: List[Example] = None):
        self.datasets = {
            'train': train,
            'dev': dev,
            'all': train + dev
        }
        if test:
            self.datasets.update({
                'test': test,
                'all': train + dev + test
            })

    def apply(self, func: Callable, *args: Any, **kwargs: Any) -> Dict[str, List[Example]]:
        """Apply an existing function to all datasets"""
        res = {}
        for k, dataset in self.datasets.items():
            res[k] = func(dataset, *args, **kwargs)
        return res
    
    def apply_(self, func: Callable, *args: Any, **kwargs: Any) -> None:
        """Apply an existing function to all datasets inplace
        and update self.datasets"""
        res = {}
        for k, dataset in self.datasets.items():
            res[k] = func(dataset, *args, **kwargs)
        self.datasets = res
