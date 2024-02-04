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
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain==0.1.3) (1.26.13)
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
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core<0.2,>=0.1.13->langchain-openai==0.0.3) (1.26.13)
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
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core<0.2,>=0.1.16->langchain_openai==0.0.5) (1.26.13)
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
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-community==0.0.15) (1.26.13)
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
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core==0.1.15) (1.26.13)
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
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langsmith==0.0.83) (1.26.13)
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
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain-core<0.2.0,>=0.1.16->langgraph==0.0.21) (1.26.13)
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
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0,>=2.0.0->wikipedia) (1.26.13)
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
import os


# def _set_if_undefined(var: str):
#     if not os.environ.get(var):
#         os.environ[var] = getpass(f"Please provide your {var}")


# # 必須APIキーの確認
# _set_if_undefined("OPENAI_API_KEY")
# _set_if_undefined("LANGCHAIN_API_KEY")
# _set_if_undefined("TAVILY_API_KEY")

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
# LangSmithの設定
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_ENDPOINT"]="https://api.smith.langchain.com"
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_PROJECT"] = "blog_supervisor_dev"

# LLM_SMART_MODEL = "gpt-3.5-turbo-1106"
# LLM_SMART_MODEL = "gpt-3.5-turbo-0125"
# LLM_SMART_MODEL = "gpt-4-1106-preview"
LLM_SMART_MODEL = "gpt-4-0125-preview"
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
class AgentDescription(TypedDict):
    name: str
    description: str
    
def create_agent(
        llm: ChatOpenAI,
        tools: list,
        system_prompt: str,
) -> AgentExecutor:
    system_prompt += "\nWork autonomously according to your specialty, using the tools available to you."
    " Do not ask for clarification."
    " Your other team members (and other teams) will collaborate with you with their own specialties."
    " You are chosen for a reason! You are one of the following team members: {team_members}."
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
    agent = create_openai_functions_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools)


def create_team_supervisor(
        llm: ChatOpenAI,
        system_prompt: str,
        members: list[AgentDescription]
) -> Runnable:
    member_names = [member["name"] for member in members]
    team_members = []
    for member in members:
        team_members.append(f"name: {member['name']}\ndescription: {member['description']}")
    options = ["FINISH"] + member_names
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
    return (
            prompt
            | llm.bind_functions(functions=[function_def], function_call="route")
            | JsonOutputFunctionsParser()
    )
```

## Researchエージェントの定義
Web検索にTavilyを利用している。 TavilyもしくはURLの直接アクセスをサポートするために、 function callingを利用したエージェントを利用


```python
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool

llm = ChatOpenAI(model_name=LLM_SMART_MODEL, 
                 temperature=0.7)
tavily_tool = TavilySearchResults(max_results=5)


@tool
def scrape_webpages(urls: list[str]) -> str:
    """Use requests and bs4 to scrape the provided web pages for detailed information."""
    loader = WebBaseLoader(urls)
    docs = loader.load()
    return "\n\n".join(
        [
            f'<Document name="{doc.metadata.get("title", "")}">\n{doc.page_content}\n</Document>'
            for doc in docs
        ]
    )


def create_research_agent() -> Runnable:
    prompt = "You are a research assistant who can search for up-to-date info using the tavily search engine."
    return create_agent(llm, [tavily_tool, scrape_webpages], prompt)

```

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
team_members = [
    {"name": RESEARCH_NODE,
     "description": "Search the web for necessary information and write articles as requested by users."},
    {"name": QUALITY_ASSURANCE_NODE,
     "description": f"Check that the quality of the article meets the criteria. If not, return feedback. The acceptability of deliverables is always determined by {QUALITY_ASSURANCE_NODE}."},
    {"name": WRITER_NODE,
     "description": "Write articles that even the world's best AI checkers would judge as written by a human."},
]


# トップレベルのステートを定義
class TopState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]
    output: str
    next: str


def create_llm_chain(llm: ChatOpenAI, system_message: str) -> Runnable:
    prompt = ChatPromptTemplate.from_messages(
        [("system", system_message), ("user", "{message}")]
    )
    chain = {"message": RunnablePassthrough()} | prompt | llm | StrOutputParser()
    return chain


# Researcherノードの定義
def research_node(state: TopState) -> dict:
    last_message = state["messages"][-1]
    result = create_research_agent().invoke({"messages": [last_message]})
    return {
        "output": result["output"],
        "messages": [AIMessage(content=result["output"])]
    }


# Writerノードの定義
def writer_node(state: TopState) -> dict:
    system_message = """You are a writing specialist.
You can write sentences that even the world's best AI checkers would judge as written by a human."""
    latest_message = state["messages"][-1].content
    chain = create_llm_chain(llm, system_message)
    result = chain.invoke(latest_message)
    return {
        "output": result,
        "messages": [AIMessage(content=result)]
    }


# 品質チェックノードの定義
def qa_node(state: TopState) -> dict:
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
    latest_output = state["output"]
    chain = create_llm_chain(llm, system_message)
    result = chain.invoke(latest_output)
    result_with_original_article = f"feedback: {result}\n\n-----\n{latest_output}"
    return {"messages": [AIMessage(content=result_with_original_article)]}


# Supervisorノードの定義
def supervisor_node(state: TopState) -> Runnable:
    prompt = """You are a supervisor tasked with managing a conversation between the following teams:
{team_members}
    
Given the following user request, respond with the worker to act next. 
Each worker will perform a task and respond with their results and status.
When finished, respond with FINISH."""
    return create_team_supervisor(llm, prompt, team_members)
```

## LangGraphの定義
LangGraphのStateGraphにノードと、ノード間を繋ぐエッジを設定する。 SUPERVISOR_NODEは次にどのノードに遷移するかを決定するため、条件付きエッジを設定する。


```python
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END

graph = StateGraph(TopState)

graph.add_node(RESEARCH_NODE, research_node)
graph.add_node(QUALITY_ASSURANCE_NODE, qa_node)
graph.add_node(WRITER_NODE, writer_node)
graph.add_node(SUPERVISOR_NODE, supervisor_node)

graph.add_edge(RESEARCH_NODE, SUPERVISOR_NODE)
graph.add_edge(QUALITY_ASSURANCE_NODE, SUPERVISOR_NODE)
graph.add_edge(WRITER_NODE, SUPERVISOR_NODE)
graph.add_conditional_edges(
    SUPERVISOR_NODE,
    lambda x: x["next"],
    {
        RESEARCH_NODE: RESEARCH_NODE,
        QUALITY_ASSURANCE_NODE: QUALITY_ASSURANCE_NODE,
        WRITER_NODE: WRITER_NODE,
        "FINISH": END,
    }
)

graph.set_entry_point(SUPERVISOR_NODE)
blog_writer = {"messages": lambda x: [HumanMessage(content=x)]} | graph.compile()

```

## LangGraphの実行
処理の流れが分かりやすいようにstream関数で実行している。 LangSmithが利用できる場合はLangSmith上で確認すると、より分かりやすい。


```python
# query = """以下の論文について、概要、新規性、数式やアルゴリズムなどの手法、実験結果、実装方法等を順番に考えながら詳しく日本語で書きなさい。AI文章チェッカーによる判定で、AIが書いたと判定されないように書くこと。
# https://arxiv.org/pdf/2401.15884.pdf
# """
query = """2024/02/05から/06までの東京の天気を順番に詳しく教えてください。また、その気象になる理由を詳しく日本語で書き教えてください。"""
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

    {'supervisor': {'next': 'research'}}
    ---
    {'research': {'output': '2024年1月から3月にかけての気象庁の長期予報によると、全国的に暖冬傾向が続く見込みです。関東甲信地方は、寒気の影響を受けにくいため、この期間の気温は「平年より高い」と予想されています。また、低気圧などの影響を受けやすいため、この期間の降水量は「平年並か多い」見込みです。\n\nこの情報に基づくと、2024年2月5日から6日までの東京の天気も、平年より暖かく、雨が降る可能性が高いことを示唆しています。しかし、正確な天気予報とその気象になる理由については、具体的なデータが提供されていないため、詳細をお伝えすることができません。\n\n気象に関する理由としては、一般的に気温が平年より高い場合、地球の温暖化の影響やエルニーニョ現象などが考えられます。また、降水量が平年並か多い場合は、気圧の配置や風向き、地域に近づく低気圧の活動性などが関係しています。これらの気象現象は、大気中の温度や湿度、地表の状態など複雑な要因が絡み合って発生します。\n\n2024年2月5日から6日の東京の具体的な天気予報とその気象になる詳しい理由を知りたい場合は、もう少し時期が近づいた際に、最新の天気予報を確認することをお勧めします。', 'messages': [AIMessage(content='2024年1月から3月にかけての気象庁の長期予報によると、全国的に暖冬傾向が続く見込みです。関東甲信地方は、寒気の影響を受けにくいため、この期間の気温は「平年より高い」と予想されています。また、低気圧などの影響を受けやすいため、この期間の降水量は「平年並か多い」見込みです。\n\nこの情報に基づくと、2024年2月5日から6日までの東京の天気も、平年より暖かく、雨が降る可能性が高いことを示唆しています。しかし、正確な天気予報とその気象になる理由については、具体的なデータが提供されていないため、詳細をお伝えすることができません。\n\n気象に関する理由としては、一般的に気温が平年より高い場合、地球の温暖化の影響やエルニーニョ現象などが考えられます。また、降水量が平年並か多い場合は、気圧の配置や風向き、地域に近づく低気圧の活動性などが関係しています。これらの気象現象は、大気中の温度や湿度、地表の状態など複雑な要因が絡み合って発生します。\n\n2024年2月5日から6日の東京の具体的な天気予報とその気象になる詳しい理由を知りたい場合は、もう少し時期が近づいた際に、最新の天気予報を確認することをお勧めします。')]}}
    ---
    {'supervisor': {'next': 'research'}}
    ---
    {'research': {'output': '2024年2月5日から6日にかけての東京の天気予報に関して、関東甲信地方では本州の南岸を進む低気圧の影響で、山沿いや山地を中心に大雪となり、東京23区を含む平地でも雪が積もる見込みと報じられています。気温が予想よりも低くなった場合は、平地でも警報級の大雪のおそれがあるため、交通への影響などが懸念されています。東京23区では2センチの雪が降る見込みで、6日夕方までの24時間に降る雪の量は、関東北部の山地で20センチから40センチ、関東北部の平地、甲信、箱根から多摩地方や秩父地方にかけてが10センチから20センチ、関東南部の平地で5センチと予測されています。\n\nこの気象現象は、本州の南岸を進む低気圧が大きな影響を与えており、それに伴う気温の低下と降雪が予想されています。このような天候条件下では、外出の際には十分な注意が必要です。また、予想よりも低い気温となることで、平地でも大雪になる可能性があるため、今後の気象情報に注意してください。', 'messages': [AIMessage(content='2024年2月5日から6日にかけての東京の天気予報に関して、関東甲信地方では本州の南岸を進む低気圧の影響で、山沿いや山地を中心に大雪となり、東京23区を含む平地でも雪が積もる見込みと報じられています。気温が予想よりも低くなった場合は、平地でも警報級の大雪のおそれがあるため、交通への影響などが懸念されています。東京23区では2センチの雪が降る見込みで、6日夕方までの24時間に降る雪の量は、関東北部の山地で20センチから40センチ、関東北部の平地、甲信、箱根から多摩地方や秩父地方にかけてが10センチから20センチ、関東南部の平地で5センチと予測されています。\n\nこの気象現象は、本州の南岸を進む低気圧が大きな影響を与えており、それに伴う気温の低下と降雪が予想されています。このような天候条件下では、外出の際には十分な注意が必要です。また、予想よりも低い気温となることで、平地でも大雪になる可能性があるため、今後の気象情報に注意してください。')]}}
    ---
    Search agent operating time:  114.615[s]



```python
print(latest_output)
```

    2024年2月5日から6日にかけての東京の天気予報に関して、関東甲信地方では本州の南岸を進む低気圧の影響で、山沿いや山地を中心に大雪となり、東京23区を含む平地でも雪が積もる見込みと報じられています。気温が予想よりも低くなった場合は、平地でも警報級の大雪のおそれがあるため、交通への影響などが懸念されています。東京23区では2センチの雪が降る見込みで、6日夕方までの24時間に降る雪の量は、関東北部の山地で20センチから40センチ、関東北部の平地、甲信、箱根から多摩地方や秩父地方にかけてが10センチから20センチ、関東南部の平地で5センチと予測されています。
    
    この気象現象は、本州の南岸を進む低気圧が大きな影響を与えており、それに伴う気温の低下と降雪が予想されています。このような天候条件下では、外出の際には十分な注意が必要です。また、予想よりも低い気温となることで、平地でも大雪になる可能性があるため、今後の気象情報に注意してください。



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

    {'supervisor': {'next': 'research'}}
    ---
    {'research': {'output': '株式会社オージス総研は、大阪ガスを母体とし、1983年に創業した情報技術（IT）の分野におけるシステムインテグレーター（SIer）としての役割を担っています。この企業は、特に社会インフラを支える領域において、その技術力とサービスを提供しており、社会がスムーズに機能するために不可欠なサービスを提供しています。資本金は4億4,000万円で、大阪ガスが100％出資しており、売上高は401億6,300万円（2020年度単体）となっています。\n\nオージス総研の提供する製品・サービスは、コンサルティングからシステム開発、IT基盤の運用・保守、基幹業務のサポート、業務分析、セキュリティに関するソリューションまで幅広く対応しています。また、技術力を活かしたIT研修・ラーニングサービスを提供し、グローバルで通用するITスキルとキャリアアップを支援しています。\n\n最近の取り組みとして、オージス総研は自然言語モデルを用いたAI採点システムを開発し、小学生向け教育サービス「カンガエMAX。」に提供を開始しました。これは採点者のスキルや判断に依存せず、客観的で一貫性を持った添削が可能になるというものです。\n\nこれからの事業展開として、オージス総研は、既存の社会インフラに関連する事業領域において、さらなる深耕と革新を進める一方で、AIやIoTなどの最新技術を活用した新たなサービス開発や、教育分野への進出など、より広いフィールドへの事業拡大を目指していると考えられます。エネルギー分野やクラウド技術を活用したプロジェクトの実績があり、今後もこれらの技術を活用したイノベーションに注力していく可能性が高いです。', 'messages': [AIMessage(content='株式会社オージス総研は、大阪ガスを母体とし、1983年に創業した情報技術（IT）の分野におけるシステムインテグレーター（SIer）としての役割を担っています。この企業は、特に社会インフラを支える領域において、その技術力とサービスを提供しており、社会がスムーズに機能するために不可欠なサービスを提供しています。資本金は4億4,000万円で、大阪ガスが100％出資しており、売上高は401億6,300万円（2020年度単体）となっています。\n\nオージス総研の提供する製品・サービスは、コンサルティングからシステム開発、IT基盤の運用・保守、基幹業務のサポート、業務分析、セキュリティに関するソリューションまで幅広く対応しています。また、技術力を活かしたIT研修・ラーニングサービスを提供し、グローバルで通用するITスキルとキャリアアップを支援しています。\n\n最近の取り組みとして、オージス総研は自然言語モデルを用いたAI採点システムを開発し、小学生向け教育サービス「カンガエMAX。」に提供を開始しました。これは採点者のスキルや判断に依存せず、客観的で一貫性を持った添削が可能になるというものです。\n\nこれからの事業展開として、オージス総研は、既存の社会インフラに関連する事業領域において、さらなる深耕と革新を進める一方で、AIやIoTなどの最新技術を活用した新たなサービス開発や、教育分野への進出など、より広いフィールドへの事業拡大を目指していると考えられます。エネルギー分野やクラウド技術を活用したプロジェクトの実績があり、今後もこれらの技術を活用したイノベーションに注力していく可能性が高いです。')]}}
    ---
    {'supervisor': {'next': 'quality_assurance'}}
    ---
    {'quality_assurance': {'messages': [AIMessage(content='feedback: Acceptable\n\nこの記事は、以下の評価基準を満たしています：\n\n- 記事は日本語で書かれています。\n- 文章は人間が書いたと判断できる自然で流暢なスタイルで書かれています。AIによる文章チェックでも、人間による執筆と判断されるような質となっています。\n- 内容がわかりやすく説明されており、株式会社オージス総研の事業内容、サービス、取り組み、および将来の展望について明快に紹介しています。\n- ユーザーの要件に応じて、特定の企業に関する情報を提供しており、目的に合致しています。\n\nしたがって、この記事は審査基準を満たしていると判断されます。\n\n-----\n株式会社オージス総研は、大阪ガスを母体とし、1983年に創業した情報技術（IT）の分野におけるシステムインテグレーター（SIer）としての役割を担っています。この企業は、特に社会インフラを支える領域において、その技術力とサービスを提供しており、社会がスムーズに機能するために不可欠なサービスを提供しています。資本金は4億4,000万円で、大阪ガスが100％出資しており、売上高は401億6,300万円（2020年度単体）となっています。\n\nオージス総研の提供する製品・サービスは、コンサルティングからシステム開発、IT基盤の運用・保守、基幹業務のサポート、業務分析、セキュリティに関するソリューションまで幅広く対応しています。また、技術力を活かしたIT研修・ラーニングサービスを提供し、グローバルで通用するITスキルとキャリアアップを支援しています。\n\n最近の取り組みとして、オージス総研は自然言語モデルを用いたAI採点システムを開発し、小学生向け教育サービス「カンガエMAX。」に提供を開始しました。これは採点者のスキルや判断に依存せず、客観的で一貫性を持った添削が可能になるというものです。\n\nこれからの事業展開として、オージス総研は、既存の社会インフラに関連する事業領域において、さらなる深耕と革新を進める一方で、AIやIoTなどの最新技術を活用した新たなサービス開発や、教育分野への進出など、より広いフィールドへの事業拡大を目指していると考えられます。エネルギー分野やクラウド技術を活用したプロジェクトの実績があり、今後もこれらの技術を活用したイノベーションに注力していく可能性が高いです。')]}}
    ---
    {'supervisor': {'next': 'FINISH'}}
    ---
    Search agent operating time:  85.525[s]



```python
print(search_output)
```

    株式会社オージス総研は、大阪ガスを母体とし、1983年に創業した情報技術（IT）の分野におけるシステムインテグレーター（SIer）としての役割を担っています。この企業は、特に社会インフラを支える領域において、その技術力とサービスを提供しており、社会がスムーズに機能するために不可欠なサービスを提供しています。資本金は4億4,000万円で、大阪ガスが100％出資しており、売上高は401億6,300万円（2020年度単体）となっています。
    
    オージス総研の提供する製品・サービスは、コンサルティングからシステム開発、IT基盤の運用・保守、基幹業務のサポート、業務分析、セキュリティに関するソリューションまで幅広く対応しています。また、技術力を活かしたIT研修・ラーニングサービスを提供し、グローバルで通用するITスキルとキャリアアップを支援しています。
    
    最近の取り組みとして、オージス総研は自然言語モデルを用いたAI採点システムを開発し、小学生向け教育サービス「カンガエMAX。」に提供を開始しました。これは採点者のスキルや判断に依存せず、客観的で一貫性を持った添削が可能になるというものです。
    
    これからの事業展開として、オージス総研は、既存の社会インフラに関連する事業領域において、さらなる深耕と革新を進める一方で、AIやIoTなどの最新技術を活用した新たなサービス開発や、教育分野への進出など、より広いフィールドへの事業拡大を目指していると考えられます。エネルギー分野やクラウド技術を活用したプロジェクトの実績があり、今後もこれらの技術を活用したイノベーションに注力していく可能性が高いです。



```python

```
