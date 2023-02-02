<details open>
<summary><h1>generaltool</h1></summary>

Library code with no dependencies.

<details>
<summary><h2>Table of Contents</h2></summary>

<pre>
<a href='#generaltool'>generaltool</a>
├─ <a href='#Dependency-Diagram-for-ManderaGeneral'>Dependency Diagram for ManderaGeneral</a>
├─ <a href='#Installation-showing-dependencies'>Installation showing dependencies</a>
├─ <a href='#Information'>Information</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Contributions'>Contributions</a>
</pre>
</details>


<details open>
<summary><h2>Dependency Diagram for ManderaGeneral</h2></summary>

```mermaid
flowchart LR
3([file]) --> 5([packager])
0([import]) --> 3([file])
2([library]) --> 3([file])
2([library]) --> 4([vector])
2([library]) --> 5([packager])
1([tool]) --> 2([library])
0([import]) --> 2([library])
click 0 "https://github.com/ManderaGeneral/generalimport"
click 1 "https://github.com/ManderaGeneral/generaltool"
click 2 "https://github.com/ManderaGeneral/generallibrary"
click 3 "https://github.com/ManderaGeneral/generalfile"
click 4 "https://github.com/ManderaGeneral/generalvector"
click 5 "https://github.com/ManderaGeneral/generalpackager"
style 1 fill:#482
```
</details>


<details open>
<summary><h2>Installation showing dependencies</h2></summary>

| `pip install`     | `generaltool`   |
|:------------------|:----------------|
| *No dependencies* | ✔️              |
</details>


<details open>
<summary><h2>Information</h2></summary>

| Package                                                      | Ver                                            | Latest Release       | Python                                                                                                                                                                                                                                                 | Platform        | Cover   |
|:-------------------------------------------------------------|:-----------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|:--------|
| [generaltool](https://github.com/ManderaGeneral/generaltool) | [0.1.0](https://pypi.org/project/generaltool/) | 2023-02-02 13:29 CET | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/), [3.10](https://www.python.org/downloads/release/python-3100/), [3.11](https://www.python.org/downloads/release/python-3110/) | Windows, Ubuntu | 99.1 %  |
</details>



<details>
<summary><h2>Attributes</h2></summary>

<pre>
<a href='https://github.com/ManderaGeneral/generaltool/blob/master/generaltool/__init__.py#L1'>Module: generaltool</a>
└─ <a href='https://github.com/ManderaGeneral/generaltool/blob/master/generaltool/enforce_literal.py#L23'>Function: enforce_literals</a>
</pre>
</details>


<details open>
<summary><h2>Contributions</h2></summary>

Issue-creation, discussions and pull requests are most welcome!
</details>



<sup>
Generated 2023-02-02 13:29 CET for commit <a href='https://github.com/ManderaGeneral/generaltool/commit/master'>master</a>.
</sup>
</details>

