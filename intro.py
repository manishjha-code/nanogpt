{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOI/rtFX7xLnm12qgVqHsdH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/manishjha-code/nanogpt/blob/main/intro.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Csq5_FNbnbYB",
        "outputId": "b4471769-f9a1-4160-ccb3-ef380b8ecfc4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2025-02-23 02:24:17--  https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt\n",
            "Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...\n",
            "Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 1115394 (1.1M) [text/plain]\n",
            "Saving to: ‘input.txt’\n",
            "\n",
            "\rinput.txt             0%[                    ]       0  --.-KB/s               \rinput.txt           100%[===================>]   1.06M  --.-KB/s    in 0.1s    \n",
            "\n",
            "2025-02-23 02:24:18 (10.8 MB/s) - ‘input.txt’ saved [1115394/1115394]\n",
            "\n"
          ]
        }
      ],
      "source": [
        "!wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "with open('input.txt','r',encoding='utf-8') as f:\n",
        "  text=f.read()"
      ],
      "metadata": {
        "id": "-sLbwe-Rntit"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print (\"length of dataset in characters : \", len(text))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Yy-_toZkn-tD",
        "outputId": "9f4b308d-6d46-4215-f090-47e26a4fcc96"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "length of dataset in characters :  1115394\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(text[:1000])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QSbLvi8CoNxp",
        "outputId": "0e517eda-16a6-4a25-b32b-a6c6c0af923e"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "First Citizen:\n",
            "Before we proceed any further, hear me speak.\n",
            "\n",
            "All:\n",
            "Speak, speak.\n",
            "\n",
            "First Citizen:\n",
            "You are all resolved rather to die than to famish?\n",
            "\n",
            "All:\n",
            "Resolved. resolved.\n",
            "\n",
            "First Citizen:\n",
            "First, you know Caius Marcius is chief enemy to the people.\n",
            "\n",
            "All:\n",
            "We know't, we know't.\n",
            "\n",
            "First Citizen:\n",
            "Let us kill him, and we'll have corn at our own price.\n",
            "Is't a verdict?\n",
            "\n",
            "All:\n",
            "No more talking on't; let it be done: away, away!\n",
            "\n",
            "Second Citizen:\n",
            "One word, good citizens.\n",
            "\n",
            "First Citizen:\n",
            "We are accounted poor citizens, the patricians good.\n",
            "What authority surfeits on would relieve us: if they\n",
            "would yield us but the superfluity, while it were\n",
            "wholesome, we might guess they relieved us humanely;\n",
            "but they think we are too dear: the leanness that\n",
            "afflicts us, the object of our misery, is as an\n",
            "inventory to particularise their abundance; our\n",
            "sufferance is a gain to them Let us revenge this with\n",
            "our pikes, ere we become rakes: for the gods know I\n",
            "speak this in hunger for bread, not in thirst for revenge.\n",
            "\n",
            "\n"
          ]
        }
      ]
    }
  ]
}