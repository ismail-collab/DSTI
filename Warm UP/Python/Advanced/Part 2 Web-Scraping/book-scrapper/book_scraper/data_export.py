from typing import List
from pathlib import Path

def export_to_csv(filepath:str, data: List) -> bool:
    """Export data to csv

    Parameters
    ----------
    filepath : str
        Full path of the file to be exported to
    data : List
        _description_

    Returns
    -------
    bool
        _description_
    """
    # Creating a path object
    pathobj = Path(filepath)

    try:
        with open(pathobj.absolute(), "w", encoding='utf-8') as f:
            for d in data:
                f.writelines(d + "\n")
        return True
            
    except Exception:
        return False