@description('Resource group name')
param resourceGroupName string

@description('Location for resources')
param location string = 'Central Israel'

@description('App Service Plan SKU')
param appServicePlanSku string = 'P1V2'

resource appServicePlan 'Microsoft.Web/serverfarms@2021-03-01' = {
  name: '${resourceGroupName}-plan'
  location: location
  sku: {
    name: appServicePlanSku
    capacity: 1
  }
}
