# csv2quiz-001
csv to quiz project

* Run [main.py](https://github.com/KanoeGitHub/csv2quiz-001/archive/refs/heads/main.zip)  
`Python main.py <csv-path> <ansewer-column-name> <question-column-name>`

* Run [main.exe](https://github.com/KanoeGitHub/csv2quiz-001/releases/tag/v0.1)  
`./main.exe <csv-path> <ansewer-column-name> <question-column-name>`

※If "test.csv" is in the same directory as the executable file, it can be executed without arguments.  
※The second and third arguments are "word" and "sent" by default.　　

---

## issues at the moment

* If there is a blank in the column value, you will get an error.
* The remaining number of questions is unknown.
* I know how many questions I answered correctly at the end, but we can't know the statistical parameter.
