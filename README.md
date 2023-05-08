# Around the Block
This project was made for COMP 590: User Interfaces at UNC by Keaw, Elaine, and Liya.

## Development
This project uses Angular, FastAPI, SQLAlchemy, and Postgres.

See [```docs/get_started.md```](https://github.com/chphoom/aroundtheblock/blob/28d230dd5292d9d6f5e37681df33d72cd3a6bb3f/docs/get_started.md) for intructions to start the development server.

## Deployment
This project is deployed on https://aroundtheblock.apps.cloudapps.unc.edu/ . Pushes to the main branch are automatically deployed.

## File Organization

### backend/models
Contains database schema.
### backend/script
Contains database scripts and scheduler script. 
### backend/script/devdata
Contains mock data for development purposes.
### backend/services
Contains backend services that get data from the database.
### backend/api
Contains API endpoints that call the functions in the service layer.
### frontend/src/app
Contains all frontend components and services. Components include an .html, .css, and .ts file for one particular part of the site. Services contain functions that call API endpoints.
### frontend/src/app/app-routing.module.ts
Contains all routes in the site.
### frontend/src/styles.css and frontend/src/custom-theme.scss
Applies site-wide styling.
