# ID Remapper

## Description
Creating a python script that takes an `input.csv` that has two rows (id, parent)
It will interpret the hierarchy from those two rows, and create an `output.csv` with the same hierarchy, but with regenerated `generated-id`s, starting at 1, and incrementing sequentially, also `generated-parent`s to match.

## Example
### `input.csv`
| id       | parent |
| -------- | -------|
| 11       |        |
| 45       | 11     |
| 72       | 11     |
| 145      | 45     |
| 188      |        |

Visualization:
* 11
  * 45
    * 145
  * 72
* 188

### `output.csv`
| id       | parent | generated-id  | generated-parent |
| -------- | -------| --------      | -------          |
| 11       |        | 1             |                  |
| 45       | 11     | 2             | 1                |
| 72       | 11     | 3             | 1                |
| 145      | 45     | 4             | 2                |
| 188      |        | 5             |                  |

Visualization:
* 1
  * 2
    * 4
  * 3
* 5
