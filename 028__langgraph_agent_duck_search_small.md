```python
!python3 --version
```

    Python 3.10.12



```python
!pip install openai==1.10.0
!pip install langchain==0.1.3
!pip install langchain-openai==0.0.3
!pip install -U langchain_openai==0.0.5
!pip install langchain-community==0.0.15
!pip install langchain-core==0.1.15
!pip install langsmith==0.0.83
!pip install langgraph==0.0.21
!pip install numexpr==2.9.0
!pip install wikipedia
!pip install -U duckduckgo-search==4.4
```

    Requirement already satisfied: openai==1.10.0 in /usr/local/lib/python3.10/dist-packages (1.10.0)
    Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.10/dist-packages (from openai==1.10.0) (3.7.1)
    Requirement already satisfied: distro<2,>=1.7.0 in /usr/lib/python3/dist-packages (from openai==1.10.0) (1.7.0)
    Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.10/dist-packages (from openai==1.10.0) (0.26.0)
    Requirement already satisfied: pydantic<3,>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from openai==1.10.0) (1.10.13)
    Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from openai==1.10.0) (1.3.0)
    Requirement already satisfied: tqdm>4 in /usr/local/lib/python3.10/dist-packages (from openai==1.10.0) (4.66.1)
    Requirement already satisfied: typing-extensions<5,>=4.7 in /usr/local/lib/python3.10/dist-packages (from openai==1.10.0) (4.9.0)
    Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->openai==1.10.0) (3.4)
    Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->openai==1.10.0) (1.2.0)
    Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai==1.10.0) (2022.12.7)
    Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai==1.10.0) (1.0.2)
    Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai==1.10.0) (0.14.0)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mRequirement already satisfied: langchain==0.1.3 in /usr/local/lib/python3.10/dist-packages (0.1.3)
    Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (6.0.1)
    Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (2.0.25)
    Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (3.9.1)
    Requirement already satisfied: async-timeout<5.0.0,>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (4.0.3)
    Requirement already satisfied: dataclasses-json<0.7,>=0.5.7 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (0.6.4)
    Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (1.33)
    Requirement already satisfied: langchain-community<0.1,>=0.0.14 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (0.0.15)
    Requirement already satisfied: langchain-core<0.2,>=0.1.14 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (0.1.18)
    Requirement already satisfied: langsmith<0.1,>=0.0.83 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (0.0.83)
    Requirement already satisfied: numpy<2,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (1.24.1)
    Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (1.10.13)
    Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (2.31.0)
    Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain==0.1.3) (8.2.3)
    Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.1.3) (23.1.0)
    Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.1.3) (6.0.4)
    Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.1.3) (1.9.4)
    Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.1.3) (1.4.1)
    Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.1.3) (1.3.1)
    Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in /usr/local/lib/python3.10/dist-packages (from dataclasses-json<0.7,>=0.5.7->langchain==0.1.3) (3.20.2)
    Requirement already satisfied: typing-inspect<1,>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from dataclasses-json<0.7,>=0.5.7->langchain==0.1.3) (0.9.0)
    Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.10/dist-packages (from jsonpatch<2.0,>=1.33->langchain==0.1.3) (2.4)
    Requirement already satisfied: anyio<5,>=3 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.14->langchain==0.1.3) (3.7.1)
    Requirement already satisfied: packaging<24.0,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.14->langchain==0.1.3) (23.2)
    Requirement already satisfied: typing-extensions>=4.2.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain==0.1.3) (4.9.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain==0.1.3) (2.1.1)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain==0.1.3) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain==0.1.3) (2.2.0)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain==0.1.3) (2022.12.7)
    Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain==0.1.3) (3.0.3)
    Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2,>=0.1.14->langchain==0.1.3) (1.3.0)
    Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2,>=0.1.14->langchain==0.1.3) (1.2.0)
    Requirement already satisfied: mypy-extensions>=0.3.0 in /usr/local/lib/python3.10/dist-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain==0.1.3) (1.0.0)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mCollecting langchain-openai==0.0.3
      Using cached langchain_openai-0.0.3-py3-none-any.whl.metadata (2.5 kB)
    Requirement already satisfied: langchain-core<0.2,>=0.1.13 in /usr/local/lib/python3.10/dist-packages (from langchain-openai==0.0.3) (0.1.18)
    Requirement already satisfied: numpy<2,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain-openai==0.0.3) (1.24.1)
    Requirement already satisfied: openai<2.0.0,>=1.6.1 in /usr/local/lib/python3.10/dist-packages (from langchain-openai==0.0.3) (1.10.0)
    Requirement already satisfied: tiktoken<0.6.0,>=0.5.2 in /usr/local/lib/python3.10/dist-packages (from langchain-openai==0.0.3) (0.5.2)
    Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (6.0.1)
    Requirement already satisfied: anyio<5,>=3 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (3.7.1)
    Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (1.33)
    Requirement already satisfied: langsmith<0.1,>=0.0.83 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (0.0.83)
    Requirement already satisfied: packaging<24.0,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (23.2)
    Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (1.10.13)
    Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (2.31.0)
    Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (8.2.3)
    Requirement already satisfied: distro<2,>=1.7.0 in /usr/lib/python3/dist-packages (from openai<2.0.0,>=1.6.1->langchain-openai==0.0.3) (1.7.0)
    Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.10/dist-packages (from openai<2.0.0,>=1.6.1->langchain-openai==0.0.3) (0.26.0)
    Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from openai<2.0.0,>=1.6.1->langchain-openai==0.0.3) (1.3.0)
    Requirement already satisfied: tqdm>4 in /usr/local/lib/python3.10/dist-packages (from openai<2.0.0,>=1.6.1->langchain-openai==0.0.3) (4.66.1)
    Requirement already satisfied: typing-extensions<5,>=4.7 in /usr/local/lib/python3.10/dist-packages (from openai<2.0.0,>=1.6.1->langchain-openai==0.0.3) (4.9.0)
    Requirement already satisfied: regex>=2022.1.18 in /usr/local/lib/python3.10/dist-packages (from tiktoken<0.6.0,>=0.5.2->langchain-openai==0.0.3) (2023.12.25)
    Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (3.4)
    Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (1.2.0)
    Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai<2.0.0,>=1.6.1->langchain-openai==0.0.3) (2022.12.7)
    Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai<2.0.0,>=1.6.1->langchain-openai==0.0.3) (1.0.2)
    Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai<2.0.0,>=1.6.1->langchain-openai==0.0.3) (0.14.0)
    Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.10/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (2.4)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (2.1.1)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (2.2.0)
    Using cached langchain_openai-0.0.3-py3-none-any.whl (28 kB)
    Installing collected packages: langchain-openai
      Attempting uninstall: langchain-openai
        Found existing installation: langchain-openai 0.0.5
        Uninstalling langchain-openai-0.0.5:
          Successfully uninstalled langchain-openai-0.0.5
    Successfully installed langchain-openai-0.0.3
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mCollecting langchain_openai==0.0.5
      Using cached langchain_openai-0.0.5-py3-none-any.whl.metadata (2.5 kB)
    Requirement already satisfied: langchain-core<0.2,>=0.1.16 in /usr/local/lib/python3.10/dist-packages (from langchain_openai==0.0.5) (0.1.18)
    Requirement already satisfied: numpy<2,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain_openai==0.0.5) (1.24.1)
    Requirement already satisfied: openai<2.0.0,>=1.10.0 in /usr/local/lib/python3.10/dist-packages (from langchain_openai==0.0.5) (1.10.0)
    Requirement already satisfied: tiktoken<0.6.0,>=0.5.2 in /usr/local/lib/python3.10/dist-packages (from langchain_openai==0.0.5) (0.5.2)
    Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (6.0.1)
    Requirement already satisfied: anyio<5,>=3 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (3.7.1)
    Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (1.33)
    Requirement already satisfied: langsmith<0.1,>=0.0.83 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (0.0.83)
    Requirement already satisfied: packaging<24.0,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (23.2)
    Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (1.10.13)
    Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (2.31.0)
    Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (8.2.3)
    Requirement already satisfied: distro<2,>=1.7.0 in /usr/lib/python3/dist-packages (from openai<2.0.0,>=1.10.0->langchain_openai==0.0.5) (1.7.0)
    Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.10/dist-packages (from openai<2.0.0,>=1.10.0->langchain_openai==0.0.5) (0.26.0)
    Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from openai<2.0.0,>=1.10.0->langchain_openai==0.0.5) (1.3.0)
    Requirement already satisfied: tqdm>4 in /usr/local/lib/python3.10/dist-packages (from openai<2.0.0,>=1.10.0->langchain_openai==0.0.5) (4.66.1)
    Requirement already satisfied: typing-extensions<5,>=4.7 in /usr/local/lib/python3.10/dist-packages (from openai<2.0.0,>=1.10.0->langchain_openai==0.0.5) (4.9.0)
    Requirement already satisfied: regex>=2022.1.18 in /usr/local/lib/python3.10/dist-packages (from tiktoken<0.6.0,>=0.5.2->langchain_openai==0.0.5) (2023.12.25)
    Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (3.4)
    Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (1.2.0)
    Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai<2.0.0,>=1.10.0->langchain_openai==0.0.5) (2022.12.7)
    Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai<2.0.0,>=1.10.0->langchain_openai==0.0.5) (1.0.2)
    Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai<2.0.0,>=1.10.0->langchain_openai==0.0.5) (0.14.0)
    Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.10/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (2.4)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (2.1.1)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (2.2.0)
    Using cached langchain_openai-0.0.5-py3-none-any.whl (29 kB)
    Installing collected packages: langchain_openai
      Attempting uninstall: langchain_openai
        Found existing installation: langchain-openai 0.0.3
        Uninstalling langchain-openai-0.0.3:
          Successfully uninstalled langchain-openai-0.0.3
    Successfully installed langchain_openai-0.0.5
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mRequirement already satisfied: langchain-community==0.0.15 in /usr/local/lib/python3.10/dist-packages (0.0.15)
    Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain-community==0.0.15) (6.0.1)
    Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.10/dist-packages (from langchain-community==0.0.15) (2.0.25)
    Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.10/dist-packages (from langchain-community==0.0.15) (3.9.1)
    Requirement already satisfied: dataclasses-json<0.7,>=0.5.7 in /usr/local/lib/python3.10/dist-packages (from langchain-community==0.0.15) (0.6.4)
    Requirement already satisfied: langchain-core<0.2,>=0.1.14 in /usr/local/lib/python3.10/dist-packages (from langchain-community==0.0.15) (0.1.18)
    Requirement already satisfied: langsmith<0.1,>=0.0.83 in /usr/local/lib/python3.10/dist-packages (from langchain-community==0.0.15) (0.0.83)
    Requirement already satisfied: numpy<2,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain-community==0.0.15) (1.24.1)
    Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langchain-community==0.0.15) (2.31.0)
    Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain-community==0.0.15) (8.2.3)
    Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.0.15) (23.1.0)
    Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.0.15) (6.0.4)
    Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.0.15) (1.9.4)
    Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.0.15) (1.4.1)
    Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.0.15) (1.3.1)
    Requirement already satisfied: async-timeout<5.0,>=4.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.0.15) (4.0.3)
    Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in /usr/local/lib/python3.10/dist-packages (from dataclasses-json<0.7,>=0.5.7->langchain-community==0.0.15) (3.20.2)
    Requirement already satisfied: typing-inspect<1,>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from dataclasses-json<0.7,>=0.5.7->langchain-community==0.0.15) (0.9.0)
    Requirement already satisfied: anyio<5,>=3 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.14->langchain-community==0.0.15) (3.7.1)
    Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.14->langchain-community==0.0.15) (1.33)
    Requirement already satisfied: packaging<24.0,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.14->langchain-community==0.0.15) (23.2)
    Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.14->langchain-community==0.0.15) (1.10.13)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-community==0.0.15) (2.1.1)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-community==0.0.15) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-community==0.0.15) (2.2.0)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-community==0.0.15) (2022.12.7)
    Requirement already satisfied: typing-extensions>=4.6.0 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain-community==0.0.15) (4.9.0)
    Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain-community==0.0.15) (3.0.3)
    Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2,>=0.1.14->langchain-community==0.0.15) (1.3.0)
    Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2,>=0.1.14->langchain-community==0.0.15) (1.2.0)
    Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.10/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.2,>=0.1.14->langchain-community==0.0.15) (2.4)
    Requirement already satisfied: mypy-extensions>=0.3.0 in /usr/local/lib/python3.10/dist-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain-community==0.0.15) (1.0.0)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mCollecting langchain-core==0.1.15
      Using cached langchain_core-0.1.15-py3-none-any.whl.metadata (6.0 kB)
    Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain-core==0.1.15) (6.0.1)
    Requirement already satisfied: anyio<5,>=3 in /usr/local/lib/python3.10/dist-packages (from langchain-core==0.1.15) (3.7.1)
    Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.10/dist-packages (from langchain-core==0.1.15) (1.33)
    Requirement already satisfied: langsmith<0.1,>=0.0.83 in /usr/local/lib/python3.10/dist-packages (from langchain-core==0.1.15) (0.0.83)
    Requirement already satisfied: packaging<24.0,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core==0.1.15) (23.2)
    Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain-core==0.1.15) (1.10.13)
    Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langchain-core==0.1.15) (2.31.0)
    Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain-core==0.1.15) (8.2.3)
    Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core==0.1.15) (3.4)
    Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core==0.1.15) (1.3.0)
    Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core==0.1.15) (1.2.0)
    Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.10/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core==0.1.15) (2.4)
    Requirement already satisfied: typing-extensions>=4.2.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain-core==0.1.15) (4.9.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core==0.1.15) (2.1.1)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core==0.1.15) (2.2.0)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core==0.1.15) (2022.12.7)
    Using cached langchain_core-0.1.15-py3-none-any.whl (229 kB)
    Installing collected packages: langchain-core
      Attempting uninstall: langchain-core
        Found existing installation: langchain-core 0.1.18
        Uninstalling langchain-core-0.1.18:
          Successfully uninstalled langchain-core-0.1.18
    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    langchain-openai 0.0.5 requires langchain-core<0.2,>=0.1.16, but you have langchain-core 0.1.15 which is incompatible.
    langgraph 0.0.21 requires langchain-core<0.2.0,>=0.1.16, but you have langchain-core 0.1.15 which is incompatible.[0m[31m
    [0mSuccessfully installed langchain-core-0.1.15
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mRequirement already satisfied: langsmith==0.0.83 in /usr/local/lib/python3.10/dist-packages (0.0.83)
    Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langsmith==0.0.83) (1.10.13)
    Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langsmith==0.0.83) (2.31.0)
    Requirement already satisfied: typing-extensions>=4.2.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langsmith==0.0.83) (4.9.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langsmith==0.0.83) (2.1.1)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langsmith==0.0.83) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langsmith==0.0.83) (2.2.0)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langsmith==0.0.83) (2022.12.7)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mRequirement already satisfied: langgraph==0.0.21 in /usr/local/lib/python3.10/dist-packages (0.0.21)
    Collecting langchain-core<0.2.0,>=0.1.16 (from langgraph==0.0.21)
      Using cached langchain_core-0.1.18-py3-none-any.whl.metadata (6.0 kB)
    Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (6.0.1)
    Requirement already satisfied: anyio<5,>=3 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (3.7.1)
    Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (1.33)
    Requirement already satisfied: langsmith<0.1,>=0.0.83 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (0.0.83)
    Requirement already satisfied: packaging<24.0,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (23.2)
    Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (1.10.13)
    Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (2.31.0)
    Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (8.2.3)
    Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (3.4)
    Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (1.3.0)
    Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (1.2.0)
    Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.10/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (2.4)
    Requirement already satisfied: typing-extensions>=4.2.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (4.9.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (2.1.1)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (2.2.0)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (2022.12.7)
    Using cached langchain_core-0.1.18-py3-none-any.whl (237 kB)
    Installing collected packages: langchain-core
      Attempting uninstall: langchain-core
        Found existing installation: langchain-core 0.1.15
        Uninstalling langchain-core-0.1.15:
          Successfully uninstalled langchain-core-0.1.15
    Successfully installed langchain-core-0.1.18
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mRequirement already satisfied: numexpr==2.9.0 in /usr/local/lib/python3.10/dist-packages (2.9.0)
    Requirement already satisfied: numpy>=1.13.3 in /usr/local/lib/python3.10/dist-packages (from numexpr==2.9.0) (1.24.1)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mRequirement already satisfied: wikipedia in /usr/local/lib/python3.10/dist-packages (1.4.0)
    Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from wikipedia) (4.12.2)
    Requirement already satisfied: requests<3.0.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from wikipedia) (2.31.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0,>=2.0.0->wikipedia) (2.1.1)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0,>=2.0.0->wikipedia) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0,>=2.0.0->wikipedia) (2.2.0)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0,>=2.0.0->wikipedia) (2022.12.7)
    Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->wikipedia) (2.5)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mRequirement already satisfied: duckduckgo-search==4.4 in /usr/local/lib/python3.10/dist-packages (4.4)
    Requirement already satisfied: docstring-inheritance>=2.1.2 in /usr/local/lib/python3.10/dist-packages (from duckduckgo-search==4.4) (2.1.2)
    Requirement already satisfied: click>=8.1.7 in /usr/local/lib/python3.10/dist-packages (from duckduckgo-search==4.4) (8.1.7)
    Requirement already satisfied: curl-cffi>=0.6.0b7 in /usr/local/lib/python3.10/dist-packages (from duckduckgo-search==4.4) (0.6.0b9)
    Requirement already satisfied: lxml>=4.9.3 in /usr/local/lib/python3.10/dist-packages (from duckduckgo-search==4.4) (4.9.4)
    Requirement already satisfied: nest-asyncio>=1.6.0 in /usr/local/lib/python3.10/dist-packages (from duckduckgo-search==4.4) (1.6.0)
    Requirement already satisfied: cffi>=1.12.0 in /usr/local/lib/python3.10/dist-packages (from curl-cffi>=0.6.0b7->duckduckgo-search==4.4) (1.16.0)
    Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from curl-cffi>=0.6.0b7->duckduckgo-search==4.4) (2022.12.7)
    Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi>=1.12.0->curl-cffi>=0.6.0b7->duckduckgo-search==4.4) (2.21)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0m


```python
import os
import random
import time

from typing import Any, List, Optional, Sequence, Tuple, Union
```


```python
from contextlib import contextmanager
from time import time

class Timer:
    """処理時間を表示するクラス
    with Timer(prefix=f'pred cv={i}'):
        y_pred_i = predict(model, loader=test_loader)
    
    with Timer(prefix='fit fold={} '.format(i)):
        clf.fit(x_train, y_train, 
                eval_set=[(x_valid, y_valid)],  
                early_stopping_rounds=100,
                verbose=verbose)

    with Timer(prefix='fit fold={} '.format(i), verbose=500):
        clf.fit(x_train, y_train, 
                eval_set=[(x_valid, y_valid)],  
                early_stopping_rounds=100,
                verbose=verbose)
    """
    def __init__(self, logger=None, format_str='{:.3f}[s]', prefix=None, suffix=None, sep=' ', verbose=0):

        if prefix: format_str = str(prefix) + sep + format_str
        if suffix: format_str = format_str + sep + str(suffix)
        self.format_str = format_str
        self.logger = logger
        self.start = None
        self.end = None
        self.verbose = verbose

    @property
    def duration(self):
        if self.end is None:
            return 0
        return self.end - self.start

    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        out_str = self.format_str.format(self.duration)
        if self.logger:
            self.logger.info(out_str)
        else:
            print(out_str)
```


```python
def load_dotenv(dotenv_path=".env"):
    with open(dotenv_path) as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            # 環境変数を設定
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

# .envファイルを読み込む
load_dotenv()
```


```python
# 環境変数を使用する
openai_api_key = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = openai_api_key
```


```python
# os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

# LLM_SMART_MODEL = "gpt-3.5-turbo-1106"
LLM_SMART_MODEL = "gpt-3.5-turbo-0125"
# LLM_SMART_MODEL = "gpt-4-0125-preview"
```

## エージェントを生成するユーティリティ関数の定義
エージェントの実装が面倒なので、LangChainのAgentExecutor


```python
from langchain_core.runnables import Runnable
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from typing import TypedDict
```


```python
# エージェントの記述情報を保持する型定義
class AgentDescription(TypedDict):
    name: str  # エージェントの名前
    description: str  # エージェントの説明
```


```python
# エージェントを生成する関数
def create_agent(
        llm: ChatOpenAI,
        tools: list,
        system_prompt: str,  # システムからエージェントへの初期プロンプト
) -> AgentExecutor:
    # システムプロンプトに自律的な働きに関する指示を追加
    system_prompt += "\nWork autonomously according to your specialty, using the tools available to you."
    " Do not ask for clarification."
    " Your other team members (and other teams) will collaborate with you with their own specialties."
    " You are chosen for a reason! You are one of the following team members: {team_members}."
    """
    あなたの専門分野に従って自律的に働いてください。使用可能なツールを使ってください
    確認のために質問をしないでください
    あなたの他のチームメンバーや他のチームも、それぞれの専門分野であなたと協力します
    あなたが選ばれたのには理由があります！あなたは以下のチームメンバーの一人です: {team_members}
    """
    # チャットプロンプトテンプレートを作成
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    # エージェントを生成
    agent = create_openai_functions_agent(llm, tools, prompt)
    # エージェントを実行するExecutorを返す
    return AgentExecutor(agent=agent, tools=tools)
```


```python
# チームのスーパーバイザーを生成する関数
def create_team_supervisor(
        llm: ChatOpenAI,
        system_prompt: str,
        members: list[AgentDescription]  # チームメンバーのリスト
) -> Runnable:
    # メンバー名のリストを生成
    member_names = [member["name"] for member in members]
    team_members = []
    # チームメンバーの名前と説明を文字列に整形
    for member in members:
        team_members.append(f"name: {member['name']}\ndescription: {member['description']}")
    options = ["FINISH"] + member_names  # 終了オプション
    # 次の役割を選択するための関数定義
    function_def = {
        "name": "route",
        "description": "Select the next role.",
        "parameters": {
            "title": "routeSchema",
            "type": "object",
            "properties": {
                "next": {
                    "title": "Next",
                    "anyOf": [
                        {"enum": options},
                    ],
                },
            },
            "required": ["next"],
        },
    }
    # スーパーバイザー用のプロンプトテンプレートを作成
    """
    システム
    上記の会話を踏まえて、次に行動すべきは誰ですか？
    それとも、終了すべきですか？次の選択肢の中から一つ選んでください: {options}
    """
    # スーパーバイザー用のプロンプトテンプレートを作成
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            (
                "system",
                "Given the conversation above, who should act next?"
                " Or should we FINISH? Select one of option: {options}",
            ),
        ]
    ).partial(options=str(options), team_members="\n\n".join(team_members))
    # スーパーバイザーの機能をバインドし、JSON出力を解析するパイプラインを作成
    return (
            prompt
            | llm.bind_functions(functions=[function_def], function_call="route")
            | JsonOutputFunctionsParser()
    )
```

## Researchエージェントの定義
Web検索はDuckDuckGoを使用している。 TavilyもしくはURLの直接アクセスをサポートするために、 function callingを利用したエージェントを利用


```python
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchResults, DuckDuckGoSearchRun
```


```python
llm = ChatOpenAI(model_name=LLM_SMART_MODEL, 
                 temperature=0.7)
# tavily_tool = TavilySearchResults(max_results=5)
duck_tool = DuckDuckGoSearchRun(max_results=5)

# Webページをスクレイピングする関数
@tool  # LangChainのツールとして関数を登録
def scrape_webpages(urls: list[str]) -> str:
    """指定されたURLのWebページから詳細情報をスクレイピングするためにrequestsとbs4を使用。"""
    loader = WebBaseLoader(urls)
    docs = loader.load()
    # ドキュメントのタイトルと内容をフォーマットして返す
    return "\n\n".join(
        [
            f'<Document name="{doc.metadata.get("title", "")}">\n{doc.page_content}\n</Document>'
            for doc in docs
        ]
    )

# Researchエージェントを生成する関数
def create_research_agent() -> Runnable:
    # あなたは、DuckDuckGo検索エンジンを使って最新の情報を検索できるリサーチアシスタントです。
    prompt = "You are a research assistant who can search for up-to-date info using the DuckDuckGo search engine."
    # return create_agent(llm, [tavily_tool, scrape_webpages], prompt)
    return create_agent(llm, [duck_tool, scrape_webpages], prompt)
```

    Task was destroyed but it is pending!
    task: <Task pending name='Task-10' coro=<AsyncDDGS.__aexit__() running at /usr/local/lib/python3.10/dist-packages/duckduckgo_search/duckduckgo_search_async.py:46>>
    /usr/lib/python3.10/asyncio/base_events.py:674: RuntimeWarning: coroutine 'AsyncDDGS.__aexit__' was never awaited
      self._ready.clear()
    RuntimeWarning: Enable tracemalloc to get the object allocation traceback
    Task was destroyed but it is pending!
    task: <Task pending name='Task-2' coro=<AsyncCurl._force_timeout() running at /usr/local/lib/python3.10/dist-packages/curl_cffi/aio.py:168> wait_for=<Future pending cb=[Task.__wakeup()]>>


## LangGraphに設定するノードの定義
ノードには関数またはRunnableが設定できる。 今回はステートの更新差分を分かりやすくするために関数を設定している。


```python
import operator
from typing import Annotated
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import BaseMessage, AIMessage
```


```python
# 各ノードの名称を定義
RESEARCH_NODE = "research"
QUALITY_ASSURANCE_NODE = "quality_assurance"
WRITER_NODE = "writer"
SUPERVISOR_NODE = "supervisor"

# チームメンバーの定義
"""
Researchノード: Web上から必要な情報を検索し、ユーザーからのリクエストに応じて記事を作成します。
Quality Assurance (QA) ノード: 記事の品質が基準を満たしているかをチェックし、満たしていない場合はフィードバックを返します。品質の受け入れ基準は常にこのノードによって決定されます。
Writerノード: 世界最高レベルのAIチェッカーでも人間が書いたと判断されるような文章を作成します。
Supervisorノード: 会話を管理し、次に動作するワーカーを指示します。全てのタスクが完了したら、「FINISH」と応答します。
"""
team_members = [
    {"name": RESEARCH_NODE,
     "description": "Search the web for necessary information and write articles as requested by users."},
    {"name": QUALITY_ASSURANCE_NODE,
     "description": f"Check that the quality of the article meets the criteria. If not, return feedback. The acceptability of deliverables is always determined by {QUALITY_ASSURANCE_NODE}."},
    {"name": WRITER_NODE,
     "description": "Write articles that even the world's best AI checkers would judge as written by a human."},
]


# システム全体の状態を管理するクラスで、メッセージリスト、出力内容、次に動作するノードを含む
class TopState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]    # メッセージのリスト、追加操作による拡張を指定
    output: str   # 処理結果の出力テキスト
    next: str    # 次に実行するノードの名称

# 与えられたメッセージに基づいて応答を生成
def create_llm_chain(llm: ChatOpenAI, system_message: str) -> Runnable:
    # プロンプトを設定
    prompt = ChatPromptTemplate.from_messages(
        [("system", system_message), ("user", "{message}")]
    )
    # プロンプト、LangChainの実行、出力の解析を連結
    chain = {"message": RunnablePassthrough()} | prompt | llm | StrOutputParser()
    return chain


# Researchノードの定義
def research_node(state: TopState) -> dict:
    # ステートから最新のメッセージを取得
    last_message = state["messages"][-1]
    # リサーチエージェントを呼び出し、結果を取得
    result = create_research_agent().invoke({"messages": [last_message]})
    # 出力と新しいメッセージをステートに反映
    return {
        "output": result["output"],
        "messages": [AIMessage(content=result["output"])]
    }


# Writerノードの定義
def writer_node(state: TopState) -> dict:
    # Writerとしての指示を含むシステムメッセージ
    # あなたは文章作成の専門家です。世界最高のAIチェッカーでさえ、人間が書いたと判断するような文章を書くことができます。
    system_message = """You are a writing specialist.
You can write sentences that even the world's best AI checkers would judge as written by a human."""
    # ステートから最新の出力を取得
    latest_message = state["messages"][-1].content
    chain = create_llm_chain(llm, system_message)
    result = chain.invoke(latest_message)
    # フィードバックと元の記事を含むメッセージをステートに反映
    return {
        "output": result,
        "messages": [AIMessage(content=result)]
    }


# 品質チェックノードの定義
def qa_node(state: TopState) -> dict:
    # 品質チェックの指示を含むシステムメッセージ
    system_message = """You are a specialist in inspecting the quality of articles. 
Inspect the article to see if it meets the following requirements:

- The article is written in Japanese.
- The writing style MUST be such that the AI sentence checker determines that it was written by a HUMAN.
- The article MUST be written in a way that is easy to understand.
- The article MUST meet the user's requirements.

If the evaluation criteria are met, write "Acceptable".
In addition, write the reason why you judged that the evaluation criteria are met.

If the evaluation criteria are not met, write "Not Acceptable".
In addition, provide feedback on what needs to be done to meet the evaluation criteria.

DO NOT make excuses such as "I can't make a decision because I am an AI".

The quality of your articles is relevant to your career.
Please be as rigorous as possible in your inspections and make sure that your feedback is helpful in making corrections.
"""
    """
    評価基準の適用例:
    1. 言語と文章スタイルの評価:
        - 記事が日本語で書かれているか。
        - 文章が人間によって書かれたとAI文章チェッカーに判断させるスタイルであるか。
    2. 内容の理解しやすさ:
        - 記事の内容が簡潔に、かつ明確に表現されているか。
        - 専門用語が適切に説明され、一般の読者も理解できるようになっているか。
    3. ユーザーの要件への適合性:
        - 記事がユーザーの要求や指定したテーマに沿っているか。
        - ユーザーが期待する情報や視点が適切に取り入れられているか。
    評価例:
    - 受理可能: 記事は全ての評価基準を満たしています。日本語で書かれており、文章スタイルは人間によるものと判断できます。
    内容は理解しやすく、ユーザーの要件にも適合しています。これらの点から、記事は受理可能と判断します。
    - 受理不可: 記事は一部の評価基準を満たしていません。特に、文章スタイルがAIによって書かれたように見える部分があります。
    また、専門用語の説明が不足しているため、内容の理解が難しい箇所があります。これらの問題を解決するためには、人間らしい表現を増やし、専門用語に対する説明を追加する必要があります。
    """
    # ステートから最新の出力を取得
    latest_output = state["output"]
    chain = create_llm_chain(llm, system_message)
    result = chain.invoke(latest_output)
    # フィードバックと元の記事を含むメッセージをステートに反映
    result_with_original_article = f"feedback: {result}\n\n-----\n{latest_output}"
    return {"messages": [AIMessage(content=result_with_original_article)]}


# Supervisorノードの定義
def supervisor_node(state: TopState) -> Runnable:
    prompt = """You are a supervisor tasked with managing a conversation between the following teams:
{team_members}
    
Given the following user request, respond with the worker to act next. 
Each worker will perform a task and respond with their results and status.
When finished, respond with FINISH."""
    """
    このシナリオに基づくと、具体的なチームメンバーのリスト（{team_members}）やユーザーの要求の内容が提供されていません。
    そのため、具体的なチームメンバーや彼らの専門分野に基づいた行動指示を出すことはできません。しかし、一般的なプロセスに従って、どのように進めるかの例を示します。
    
    1. ユーザーの要求の理解: 最初に、ユーザーの要求を正確に理解し、どのチームが関連するかを特定します。
    2. タスクの割り当て: ユーザーの要求に基づき、適切な専門知識を持つチームメンバーにタスクを割り当てます。
    3. 作業の進行: 各ワーカーは指定されたタスクを実行し、結果とステータスを報告します。
    4. 結果の評価: 各ワーカーからの結果を評価し、必要に応じて追加の作業を指示するか、またはFINISHと応答します。
    """
    """
    例えば、ユーザーの要求が「ウェブサイトのデザインの改善」に関するものである場合、デザインチームのメンバーが最初に行動すべきです。
    デザインの提案が完了したら、技術チームがその実装を行い、最終的なレビューを経てプロジェクトが完了します。
    
    応答例:
    もしユーザーの要求が具体的に技術的なサポートを必要としている場合、「技術チームのメンバー」が次に行動すべきです。
    ユーザーの要求がコンテンツの作成や校正に関するものである場合、「コンテンツチームのメンバー」が次に行動すべきです。
    すべてのタスクが完了し、ユーザーの要求が満たされたと判断される場合、応答は「FINISH」です。
    
    これはあくまで例で実際の対応は要求と設定したメンバーのリストに依存します
    """
    return create_team_supervisor(llm, prompt, team_members)
```

## LangGraphの定義

LangGraphのStateGraphにノードと、ノード間を繋ぐエッジを設定する。 SUPERVISOR_NODEは次にどのノードに遷移するかを決定するため、条件付きエッジを設定する。

![node_agent.JPG](./node_agent.JPG)


```python
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END

# StateGraphのインスタンスを作成し、TopState型を使用して初期化
graph = StateGraph(TopState)

# ノードをグラフに追加。各ノードは特定の関数に紐付けられている
graph.add_node(RESEARCH_NODE, research_node)  # Researchノード
graph.add_node(QUALITY_ASSURANCE_NODE, qa_node)  # 品質保証(QA)ノード
graph.add_node(WRITER_NODE, writer_node)  # Writerノード
graph.add_node(SUPERVISOR_NODE, supervisor_node)  # Supervisorノード

# 各ノードからSupervisorノードへのエッジを追加
graph.add_edge(RESEARCH_NODE, SUPERVISOR_NODE)
graph.add_edge(QUALITY_ASSURANCE_NODE, SUPERVISOR_NODE)
graph.add_edge(WRITER_NODE, SUPERVISOR_NODE)

# Supervisorノードから他のノードへの条件付きエッジを追加
graph.add_conditional_edges(
    SUPERVISOR_NODE,  # 条件付きエッジの起点
    lambda x: x["next"],  # 条件式。ステートの"next"フィールドを使用して遷移先を決定
    {
        RESEARCH_NODE: RESEARCH_NODE,  # Researchノードへの遷移
        QUALITY_ASSURANCE_NODE: QUALITY_ASSURANCE_NODE,  # QAノードへの遷移
        WRITER_NODE: WRITER_NODE,  # Writerノードへの遷移
        "FINISH": END,  # "FINISH"が選択された場合、グラフの実行を終了
    }
)

# エントリーポイントをSupervisorノードに設定
graph.set_entry_point(SUPERVISOR_NODE)

# グラフをコンパイルし、ブログライターのフローを定義
# HumanMessageを入力として受け取り、定義されたグラフを通じて処理を行う
blog_writer = {"messages": lambda x: [HumanMessage(content=x)]} | graph.compile()
```

## LangGraphの実行
処理の流れが分かりやすいようにstream関数で実行している。 LangSmithが利用できる場合はLangSmith上で確認すると、より分かりやすい。


```python
query = """
以下の論文サイトについて、概要、新規性、数式やアルゴリズムなどの手法、実験結果、実装方法等を順番に考えながら詳しく日本語で書きなさい。
https://osu-nlp-group.github.io/TravelPlanner/
"""
with Timer(prefix=f'Search agent operating time: '):
    latest_output = ""
    cnt = 0
    for s in blog_writer.stream(query, {"recursion_limit": 100}):
        if cnt == 4:
            break
        if "__end__" not in s:
            print(s)
            print("---")
            writing_output = (
                    s.get(RESEARCH_NODE, {}).get("output") or
                    s.get(WRITER_NODE, {}).get("output")
            )
            if writing_output:
                latest_output = writing_output
        cnt += 1
        print(cnt)
```

    {'supervisor': {'next': 'research'}}
    ---
    1
    {'research': {'output': '### 概要\n\n**TravelPlanner**は、言語エージェントの実世界での計画能力を評価するために設計された包括的なベンチマークです。このベンチマークは、旅行計画をテスト環境として採用し、関連する情報を慎重に作成してデータ汚染を最小限に抑えます。各クエリには単一の正解が存在せず、複数の事前定義された評価スクリプトを使用して、言語エージェントがクエリで示された暗黙の常識と明示的なユーザーのニーズ（つまり、常識制約とハード制約）に沿った計画を効果的に作成できるかを評価します。TravelPlannerは、旅行日数とハード制約の量を通じて計画の幅と深さを変化させることにより、言語エージェントの能力を評価します。\n\n### 新規性\n\nTravelPlannerは、言語エージェントが実世界のシナリオで計画能力を発揮するために、多様なツールを使用して情報を収集し、制約を満たしながら合理的な旅行計画を立てることができるかどうかを評価するために設計されています。このベンチマークは、環境制約、常識制約、およびハード制約という3種類の制約を設計し、実世界のアプリケーションの観点から評価します。1,225のクエリを含むTravelPlannerは、複雑な計画の幅と深さの両方をテストするように設計されています。\n\n### 手法\n\nTravelPlannerでは、言語エージェントは与えられたクエリに基づいて、交通手段、毎日の食事、観光地、および各日の宿泊施設を含む包括的な計画を立てることが期待されています。このベンチマークは、環境制約、常識制約、およびハード制約の3種類の制約を用いて、言語エージェントがこれらの制約を満たしながら合理的な旅行計画を立てることができるかどうかを評価します。\n\n### 実験結果\n\n実験結果は、異なる大規模言語モデル(Large Language Models, LLMs)と計画戦略に対するTravelPlannerの検証セットとテストセットでの主要な結果を示しています。また、GPT-4-Turboを使用した場合のツール使用エラーの分布、制約合格率、およびエージェントと参照の間の異なるツール使用数の比較も提供されています。\n\n### 実装方法\n\nTravelPlannerデータセットは、訓練セット、検証セット、テストセットに分割されています。訓練セットには45のクエリプランペアが含まれ、検証セットには180のクエリが含まれ、テストセットには1,000のランダムに分布したクエリが含まれています。また、ツール使用のシナリオとしてGPT-4-Turbo + ReAct、単独計画のシナリオとしてGPT-4-Turbo + Direct PlanningおよびGPT-4-Turbo + Reflexion Planningが紹介されています。これらの結果は、言語エージェントが実世界の計画課題に対してどのように対応できるかを示しています。', 'messages': [AIMessage(content='### 概要\n\n**TravelPlanner**は、言語エージェントの実世界での計画能力を評価するために設計された包括的なベンチマークです。このベンチマークは、旅行計画をテスト環境として採用し、関連する情報を慎重に作成してデータ汚染を最小限に抑えます。各クエリには単一の正解が存在せず、複数の事前定義された評価スクリプトを使用して、言語エージェントがクエリで示された暗黙の常識と明示的なユーザーのニーズ（つまり、常識制約とハード制約）に沿った計画を効果的に作成できるかを評価します。TravelPlannerは、旅行日数とハード制約の量を通じて計画の幅と深さを変化させることにより、言語エージェントの能力を評価します。\n\n### 新規性\n\nTravelPlannerは、言語エージェントが実世界のシナリオで計画能力を発揮するために、多様なツールを使用して情報を収集し、制約を満たしながら合理的な旅行計画を立てることができるかどうかを評価するために設計されています。このベンチマークは、環境制約、常識制約、およびハード制約という3種類の制約を設計し、実世界のアプリケーションの観点から評価します。1,225のクエリを含むTravelPlannerは、複雑な計画の幅と深さの両方をテストするように設計されています。\n\n### 手法\n\nTravelPlannerでは、言語エージェントは与えられたクエリに基づいて、交通手段、毎日の食事、観光地、および各日の宿泊施設を含む包括的な計画を立てることが期待されています。このベンチマークは、環境制約、常識制約、およびハード制約の3種類の制約を用いて、言語エージェントがこれらの制約を満たしながら合理的な旅行計画を立てることができるかどうかを評価します。\n\n### 実験結果\n\n実験結果は、異なる大規模言語モデル(Large Language Models, LLMs)と計画戦略に対するTravelPlannerの検証セットとテストセットでの主要な結果を示しています。また、GPT-4-Turboを使用した場合のツール使用エラーの分布、制約合格率、およびエージェントと参照の間の異なるツール使用数の比較も提供されています。\n\n### 実装方法\n\nTravelPlannerデータセットは、訓練セット、検証セット、テストセットに分割されています。訓練セットには45のクエリプランペアが含まれ、検証セットには180のクエリが含まれ、テストセットには1,000のランダムに分布したクエリが含まれています。また、ツール使用のシナリオとしてGPT-4-Turbo + ReAct、単独計画のシナリオとしてGPT-4-Turbo + Direct PlanningおよびGPT-4-Turbo + Reflexion Planningが紹介されています。これらの結果は、言語エージェントが実世界の計画課題に対してどのように対応できるかを示しています。')]}}
    ---
    2
    {'supervisor': {'next': 'FINISH'}}
    ---
    3
    4
    Search agent operating time:  94.119[s]



```python
# DuckDuckago検索版
print(latest_output)
```

    ### 概要
    
    **TravelPlanner**は、言語エージェントの実世界での計画能力を評価するために設計された包括的なベンチマークです。このベンチマークは、旅行計画をテスト環境として採用し、関連する情報を慎重に作成してデータ汚染を最小限に抑えます。各クエリには単一の正解が存在せず、複数の事前定義された評価スクリプトを使用して、言語エージェントがクエリで示された暗黙の常識と明示的なユーザーのニーズ（つまり、常識制約とハード制約）に沿った計画を効果的に作成できるかを評価します。TravelPlannerは、旅行日数とハード制約の量を通じて計画の幅と深さを変化させることにより、言語エージェントの能力を評価します。
    
    ### 新規性
    
    TravelPlannerは、言語エージェントが実世界のシナリオで計画能力を発揮するために、多様なツールを使用して情報を収集し、制約を満たしながら合理的な旅行計画を立てることができるかどうかを評価するために設計されています。このベンチマークは、環境制約、常識制約、およびハード制約という3種類の制約を設計し、実世界のアプリケーションの観点から評価します。1,225のクエリを含むTravelPlannerは、複雑な計画の幅と深さの両方をテストするように設計されています。
    
    ### 手法
    
    TravelPlannerでは、言語エージェントは与えられたクエリに基づいて、交通手段、毎日の食事、観光地、および各日の宿泊施設を含む包括的な計画を立てることが期待されています。このベンチマークは、環境制約、常識制約、およびハード制約の3種類の制約を用いて、言語エージェントがこれらの制約を満たしながら合理的な旅行計画を立てることができるかどうかを評価します。
    
    ### 実験結果
    
    実験結果は、異なる大規模言語モデル(Large Language Models, LLMs)と計画戦略に対するTravelPlannerの検証セットとテストセットでの主要な結果を示しています。また、GPT-4-Turboを使用した場合のツール使用エラーの分布、制約合格率、およびエージェントと参照の間の異なるツール使用数の比較も提供されています。
    
    ### 実装方法
    
    TravelPlannerデータセットは、訓練セット、検証セット、テストセットに分割されています。訓練セットには45のクエリプランペアが含まれ、検証セットには180のクエリが含まれ、テストセットには1,000のランダムに分布したクエリが含まれています。また、ツール使用のシナリオとしてGPT-4-Turbo + ReAct、単独計画のシナリオとしてGPT-4-Turbo + Direct PlanningおよびGPT-4-Turbo + Reflexion Planningが紹介されています。これらの結果は、言語エージェントが実世界の計画課題に対してどのように対応できるかを示しています。



```python
# query = """以下の論文について、概要、新規性、数式やアルゴリズムなどの手法、実験結果、実装方法等を順番に考えながら詳しく日本語で書きなさい。AI文章チェッカーによる判定で、AIが書いたと判定されないように書くこと。
# https://arxiv.org/pdf/2401.15884.pdf
# """
query = """2024/02/06から/07までの東京の天気を順番に詳しく教えてください。また、その気象になる理由を詳しく日本語で書き教えてください。"""
with Timer(prefix=f'Search agent operating time: '):
    latest_output = ""
    cnt = 0
    for s in blog_writer.stream(query, {"recursion_limit": 100}):
        if cnt == 4:
            break
        if "__end__" not in s:
            print(s)
            print("---")
            writing_output = (
                    s.get(RESEARCH_NODE, {}).get("output") or
                    s.get(WRITER_NODE, {}).get("output")
            )
            if writing_output:
                latest_output = writing_output
        cnt += 1
```


```python
print(latest_output)
```

    2024年2月6日から7日までの東京の天気は以下の通りです：
    
    - 2月6日：最高気温10°C、最低気温1°C、曇りで日中最高気温は10°C、降水確率あり、風速15.0 mph（やや強い風）、風向360度（北）、雲の高さ5,000 ft、日照時間6時間、降水量58 mm。
    - 2月7日：天気予報の詳細は提供されていませんが、降水確率や気温の変化が予想されます。
    
    東京でこのような天候になる理由について、日本気象庁によると、2月5日から6日に関東甲信地方で大雪が予想されており、東京でも雪が降る可能性があります。この期間の天候は寒冷であり、寒気が流れ込んできているため、積雪と凍結した道路が発生する可能性があります。
    
    以上が2024年2月6日から7日までの東京の天気とその気象になる理由に関する情報です。



```python
# 直接的にリンクを設定しないと無限ループに陥る可能性があります
```


```python
def search_agent(query):
    latest_output = ""
    for s in blog_writer.stream(query, {"recursion_limit": 100}):
        if "__end__" not in s:
            print(s)
            print("---")
            writing_output = (
                    s.get(RESEARCH_NODE, {}).get("output") or
                    s.get(WRITER_NODE, {}).get("output")
            )
            if writing_output:
                latest_output = writing_output
    return latest_output
```


```python
query = """以下の企業について、行っている事業と分野、これからやりそうなことや現在やっていいそうな事業を日本語で書きなさい。AI文章チェッカーによる判定で、AIが書いたと判定されないように書くこと。
https://www.ogis-ri.co.jp/
"""
```


```python
with Timer(prefix=f'Search agent operating time: '):
    search_output = search_agent(query)
```

    {'supervisor': {'next': 'writer'}}
    ---
    {'writer': {'output': '株式会社オージス総研は、経営課題の解決を支援するコンサルティング事業を展開しています。主に情報通信技術やコンサルティング分野で活動しており、今後はデジタルトランスフォーメーション関連のサービスや、クラウドテクノロジーを活用した新たな事業展開が期待されています。', 'messages': [AIMessage(content='株式会社オージス総研は、経営課題の解決を支援するコンサルティング事業を展開しています。主に情報通信技術やコンサルティング分野で活動しており、今後はデジタルトランスフォーメーション関連のサービスや、クラウドテクノロジーを活用した新たな事業展開が期待されています。')]}}
    ---
    {'supervisor': {'next': 'FINISH'}}
    ---
    Search agent operating time:  2.935[s]



```python
print(search_output)
```

    株式会社オージス総研は、経営課題の解決を支援するコンサルティング事業を展開しています。主に情報通信技術やコンサルティング分野で活動しており、今後はデジタルトランスフォーメーション関連のサービスや、クラウドテクノロジーを活用した新たな事業展開が期待されています。



```python

```
