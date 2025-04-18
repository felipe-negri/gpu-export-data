Turing Smart Screen - Coletando Dados da GPU
Este projeto permite coletar informações sobre a utilização da GPU NVIDIA dentro de uma VM com passthrough de GPU e exibir essas informações para um sistema de monitoramento. O script usa o Flask para criar um servidor HTTP que expõe os dados da GPU via API.

📜 Objetivo
A ideia é coletar dados da GPU (como uso, memória, etc.) da VM com o NVIDIA passthrough e disponibilizar esses dados para serem consumidos por outra instância ou serviço no Proxmox ou em qualquer outro sistema que precise dessa informação.
