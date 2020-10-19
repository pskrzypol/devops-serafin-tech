#!/bin/bash

az appservice plan create --name asp-devops-serafin-tech --resource-group serafin-testing --location northeurope --sku F1 --subscription Pay-As-You-Go

az webapp create --name devops-serafin-tech --resource-group serafin-testing --plan asp-devops-serafin-tech --runtime "python|3.6"

