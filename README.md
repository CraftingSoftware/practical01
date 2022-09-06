# Using Git on Your Own

## Due Date

September 9th, 2022 by midnight

## Introduction

In this practical assignment, you will fix and extend a sorting program, `sort.py`. By the end of this exercise, you should have the tools and knowledge to be able to demonstrate mastery of the following essential technical skills of software engineering:

- How to create small, focused commits
- How to write good commit messages

## Instructions

### Installing Tools

For this course, you must use an integrated development environment (IDE), such as [Visual Studio Code](https://code.visualstudio.com/) or [Atom](https://atom.io/), and you must write programs in the [Python programming language](https://www.python.org/). Thus, if you do not have an IDE installed on your laptop, please install either Visual Studio Code or Atom. If you do not have Python installed on your laptop, please install Python 3 using the [installation guide for your operating system](https://docs.python-guide.org/starting/installation/#python-3-installation-guides).

### Fixing a Bug

The sorting program, `sort.py`, should take in a list of numbers as arguments and print the numbers in ascending order. Beside each number should be its position.

```console
$ python sort.py 23 4 15 8 16 42
[0] 4
[1] 8
[2] 15
[3] 16
[4] 23
[5] 42
```

However, when you run `sort.py`, you will notice that it does not produce the expected output. In fact, you will see an error.

```console
NameError: name 'sys' is not defined
```

Please fix this bug in `sort.py` by importing the `sys` module. Then, in your IDE, open the version control feature--in Visual Studio Code this will be the [Source Control tab](https://code.visualstudio.com/docs/editor/versioncontrol#_git-support) in the left sidebar and in Atom this will be the [Git panel](https://flight-manual.atom.io/using-atom/sections/github-package/#github-package) that can be toggled in the Status Bar in the lower-right corner. You should see `sort.py` in the list of unstaged changes (just "Changes" in Visual Studio Code).

Click on `sort.py` in the list of unstaged changes. This will open the changes, or "diffs", that you have made to the file. Since you have made only one change to `sort.py`, you can stage the entire file. To do this in Visual Studio Code, hover over `sort.py` in the list of unstaged changes and click the + icon. To do this in Atom, you can either double-click `sort.py` in the list of unstaged changes or single-click `sort.py` and press `Enter`. This will move `sort.py` into the list of staged changes. For those familiar with using the `git` command-line utility, this action is equivalent to running `git add sort.py`.

Next, in the commit message box, type "Import missing sys module". This will be the first line of the commit message, which is also referred to as its subject line. Most of the time, just a subject line will suffice. However, there may be cases where you want to attach more detail to a commit. You can do so in the body of the commit message, which is separated from the subject line by one empty line.

Notice that this commit message, "Import missing sys module", abides by [the seven rules of a great Git commit message](https://cbea.ms/git-commit/). Specifically, it is less than 50 characters long, it is capitalized, it does not end with a period, and it uses the [imperative mood](https://en.wikipedia.org/wiki/Imperative_mood). Notice also that it describes not only *what* change was made, but also *why*.

Contrast it to the following alternative, but inferior commit messages.

1. "Updates". This commit message does not describe the change in the commit.
1. "Importing missing sys module.". The subject line of this commit message contains 4 characters--"ing" and "."--that add nothing to its meaning. While 4 characters may not seem like many, if the subject line is 50 characters long (i.e. the longest recommended length), these useless characters make up nearly 10% of the subject line.
1. "Import sys module". This commit message lacks detail about why the change was made.

Once you have finished typing the commit message, you can create the commit. In Visual Studio Code, you can do this by clicking the checkmark right above the commit message box. In Atom, you can create the commit by clicking the button directly below the commit message box. For those familiar with using the `git` command-line utility, this action is equivalent to running `git commit -m "Import missing sys module"`.

### Fixing Additional Bugs

When you run `sort.py` again, you will notice that it still does not produce the expected output. Please track down and fix the two additional bugs in `sort.py`. You may need to refer to the Python documentation on [`sys.argv`](https://docs.python.org/3/library/sys.html?highlight=argv#sys.argv) and the [`enumerate`](https://docs.python.org/3/library/functions.html?highlight=enumerate#enumerate) built-in function. As you are fixing these bugs, do not yet perform any Git actions in your IDE.

Once you have completed the bug fixes, open the version control feature in your IDE and click on `sort.py` in the list of unstaged changes to see the diff. Notice that `sort.py` contains two hunks, or groups of differing lines--one per bug fix. You may be tempted to stage the entire file and create a commit with the message "Fix bugs". However, if you want to revert one of these bug fixes in the future, creating a "Fix bugs" commit would first make it difficult to locate the commit with the bug fix you want to revert and then impossible to `git revert` the one bug fix without reverting the other.

Instead, you should commit the two hunks in two separate commits to keep each commit small and focused. In both IDEs, you can select a hunk by highlighting it. In Visual Studio Code, you can stage the selected hunk by right-clicking, then clicking the "Stage Selected Ranges" item in the menu that appears. In Atom, you can stage the selected hunk by clicking the "Stage Selection" button.

For each hunk, please write a commit message that abides by [the seven rules of a great Git commit message](https://cbea.ms/git-commit/) and that describes the change and why it was made. Then, create a commit. You should have created two commits in this step.

### Adding a Feature

In addition to sorting in ascending order, `sort.py` should be able to sort numbers in descending order. The user should be able to indicate whether the order should be descending by passing in the word `desc` as a command-line argument to `sort.py`.

```console
$ python sort.py desc 23 4 15 8 16 42
[0] 42
[1] 23
[2] 16
[3] 15
[4] 8
[5] 4
```

Please implement this feature and commit it using best commit practices.

### Reflection

Answer all questions in `writing/reflection.md`. As you do, commit your changes using best commit practices. Instead of creating a commit at the end with the message, "Answer reflection questions", you should commit after answering each question and describe your changes in the commit messages. For instance, after you answer the first question, you might create a commit with the message, "Reflect on past commit practices".

## Running GatorGrader

You can gain an approximation of your progress on this assignment by running [GatorGrader](https://github.com/GatorEducator/gatorgrader).

```bash
gatorgrade --config config/gatorgrade.yml
```

## Assessment Strategy

This assignment will be assessed based on the following components:

- Percentage of Passing GatorGrader Checks: Students are encouraged to repeatedly try to implement a Python program that passes all of the GatorGrader checks by, for instance, creating a program that produces the correct output. Students should also repeatedly revise their technical writing to ensure that it also passes all of GatorGrader's checks about, for instance, the length of its content.
- GitHub Actions Build Status: Since additional checks on the source code and/or technical writing may be encoded in GitHub Actions and, moreover, all of the GatorGrader checks are also run in GitHub Actions, students will receive a checkmark grade if their last before-the-deadline build passes and a green ✔ appears in their GitHub commit log instead of a red ✗. As with the previous grading component, students are encouraged to repeatedly revise their source code and technical writing in an attempt to get their GitHub Actions build to pass. Please note that spell checking, which is run in GitHub Actions, can often flag proper nouns or other real words if the dictionary it uses does not contain them; to get your GitHub Actions build to pass, you may need to add correctly spelled words that are incorrectly flagged as "unknown" to the list of words in `.github/cspell.json`.
- Mastery of Technical Writing: Students will also receive a checkmark grade when the responses to the technical writing questions presented in the `writing/reflection.md` reveal a mastery of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing technically accurate answers.
- Mastery of Technical Knowledge and Skills: Students will also receive a checkmark grade when their GitHub repository reveals that they have mastered all of the learning objectives of this assignment. As a part of this grade, the instructor will assess aspects of the assignment including, but not limited to, the inclusion of effective source code comments, evidence of best commit practices, correct use of Docker, and correct installation and use of a Python development environment.
