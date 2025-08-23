{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPSU/fEadE+kskh/Tb4pByx"
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
      "source": [
        "# Segundo ejemplo en python\n",
        "\n",
        "* Saber si un número es positivo o negativo."
      ],
      "metadata": {
        "id": "Ozhu2_ba0r7W"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numero = int(input(\"Digite un número: \"))\n",
        "\n",
        "if numero == 0:\n",
        "  print(\"El número es cero\")\n",
        "elif numero > 0:\n",
        "  print(\"El número es positivo\")\n",
        "else:\n",
        "  print(\"El número es negativo\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PtQ5GryO08Am",
        "executionInfo": {
          "status": "ok",
          "timestamp": 1755347118634,
          "user_tz": 300,
          "elapsed": 3477,
          "user": {
            "displayName": "Jesús Ariel Gonzalez Bonilla",
            "userId": "16495358351557619651"
          }
        },
        "outputId": "396b7ac9-6f25-4fa2-fe76-9e5e6f7245c6"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite un número: 21\n",
            "El número es positivo\n"
          ]
        }
      ]
    }
  ]
}

