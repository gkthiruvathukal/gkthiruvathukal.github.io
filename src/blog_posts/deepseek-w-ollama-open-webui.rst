:blogpost: true
:date: January 28, 2025
:category: Blog Post
:tags: Artificial Intelligence, 01-28-2025
:nocomments:

########################################################
*Running Deepseek-R1 Locally with Ollama and Open WebUI*
########################################################

:bdg-primary:`Blog Post` :bdg-primary-line:`Artificial Intelligence`

************************
DeepSeek R1 Has Dropped
************************

DeepSeek-R1 :cite:p:`guo_deepseek-r1_2025` is the latest open-source LLM model
and the first [1]_ open-source *reasoning* model. While I'm unfamiliar with the
intricacies of reasoning models, the gist of it is that these LLMs
"think through" the problem before responding. In other words, as part
of the output that you get from your prompt, you also get the chain of
thought :cite:p:`wei_chain-of-thought_2022` that supports the reasoning behind
the model's output. This provides context as to why the model generated its
final output.

To be clear, I wouldn't call these models self-explaining; at the end of
the day, LLMs are still considered black boxes that generate text based
on statistical and mathematical computations. Just because DeepSeek-R1
"thinks through" a problem does not mean that it is sentient, accurate, or
correct. There is still a need for human-in-the-loop style usage when leveraging
these models to evaluate the correctness of the response.

With the context and clarification out of the way, how can you leverage
DeepSeek-R1 locally? And more broadly, how do you do so with many
open-source LLMs?

******************************
Ollama As An Inference Server
******************************

You leverage Ollama [2]_, an open-source *inference engine* that is designed
to work with *quantized LLMs* :cite:p:`han_deep_2016` via the
*GGUF file format* [3]_ on models hosted on the *Ollama Model Hub* [4]_ .

An inference engine is a utility to run machine and deep learning
models efficiently by optimizing the model's underlying computational
graph.

The computational graph is similar to a program's call graph (or the
order in which instructions are executed) but for mathematics

Quantized LLMs are large language models whose computational graph
relies on either a reduced number of bits to represent floating point
numbers or integers.

Deep learning models are often trained using bit widths of 64. 128, or
higher to represent the nuances of data that can be represented at a
given time. Reducing the bit width or precision (e.g., floating point
representation to integer representation) often improves the latency
of the model (measured in tokens per second) at the cost of precise
answers.

Ollama provides a very simple interface to get started with using LLMs
locally. Alternatives do exist [5]_ but the tooling surrounding Ollama is
extensive and well-documented, so it is my preferred choice when running LLMs
locally.

As Ollama is a command-line utility it can be difficult to leverage
tooling such as document and image reasoning, web searching, retrieval
augmented generation (RAG) :cite:p:`lewis_retrieval-augmented_2020`, and
multi-modal data analysis without having to develop your own interface. This is
where GUI interfaces such as Open WebUI [6]_ fill the gap.

***********
Open WebUI
***********

Open WebUI is a self-hostable application that communicates to Ollama
via Ollama's HTTP REST API. It provides a ChatGPT-like interface that I
find familiar while exposing existing ChatGPT features such as image
generation, document reasoning, RAG, and web search. It also supports
new features like the ability to chain multiple models together to
provide one model with a prompt, and then automatically pass the
response of that model into a second or third LLM for post-processing! I
think it's a neat project and an exemplar of the Ollama ecosystem.

***********************
Putting It All Together
***********************

Having gone through all of this now, how can we install these tools?

If you are on an M series Mac, you should install Ollama locally and
ignore all references to Ollama docker installation hereafter. This is
because Ollama via Docker does not support M series Mac GPU
acceleration, but the compiled binary does [7]_ .

For everyone else, I recommend installing Ollama and Open Web UI via
Docker Compose via this YAML file:

.. dropdown:: ``docker-compose.yml`` file contents

   .. code:: yaml

      version: '3.8'
      name: ai

      services:
      ollama:
         container_name: ollama
         image: ollama/ollama:0.5.7
         restart: always
         networks:
            - ollama-network
         ports:
            - "11434:11434"
         volumes:
            - ollama:/root/.ollama
         deploy:
            resources:
            reservations:
               devices:
                  - driver: nvidia
                  capabilities: [gpu]

      open-webui:
         container_name: open-webui
         image: ghcr.io/open-webui/open-webui:0.5.7
         restart: always
         extra_hosts:
            - "host.docker.internal:host-gateway"
         networks:
            - ollama-network
         ports:
            - "3000:8080"
         volumes:
            - open-webui:/app/backend/data

      networks:
      ollama-network:
         external: false

      volumes:
      ollama:
      open-webui:

Copy this to a ``docker-compose.yml`` file and then run:

.. dropdown:: Using ``docker compose`` to setup services

   .. code:: shell

      docker compose --file ./docker-compose.yml create
      docker compose --file ./docker-compose.yml start

This installs Ollama at its latest version (as of writing) with NVIDIA
GPU acceleration support [8]_ . It also installs the latest
version of Open WebUI (as of writing). The Ollama HTTP REST API is
exposed on port ``11434`` and Open WebUI is exposed on port ``3000``.

Once installed run the following command to install DeepSeek-R1 from
Ollama's Model Hub:

.. dropdown:: Pulling DeepSeek-R1 from the Ollama model hub

   .. code:: shell

      docker compose --file ./docker-compose.yml exec ollama ollama pull deepseek-r1:7b

Then refresh your browser's connection to Open WebUI (via
http://localhost:3000) and you should be able to start using DeepSeek R1
locally!

*************
Bibliography
*************

.. bibliography::
   :filter: false

   guo_deepseek-r1_2025
   han_deep_2016
   lewis_retrieval-augmented_2020
   wei_chain-of-thought_2022

.. [1] To my knowledge

.. [2] `<https://github.com/ollama/ollama>`_

.. [3] `<https://github.com/ggml-org/ggml/blob/master/docs/gguf.md>`_

.. [4] `<https://ollama.com/search>`_

.. [5] See `vllm <https://vllm.ai>`_

.. [6] `<https://github.com/open-webui/open-webui>`_

.. [7]

   You can read about it
   `here <https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image>`__.

.. [8]

   If you don't have NVIDIA GPU support for Docker or are using a different
   GPU vendor or intend to run this on CPU, see this post from
   `Ollama <https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image>`_.
