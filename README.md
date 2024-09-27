[![Publish Docker image](https://github.com/Gniamor/Eval-M2/actions/workflows/docker-deploy.yml/badge.svg)](https://github.com/Gniamor/Eval-M2/actions/workflows/docker-deploy.yml)

# Eval-M2

## Groq API

![image](https://github.com/user-attachments/assets/409d0947-ccd7-43bb-8086-7d8d452719d4)

voici le capture que le serveur croq a bien fonctionné a démarré et est fonctionnel
L'API a bien été pris en compte


## Dockerize Fast Api

voici le capture que le serveur croq a bien fonctionné a démarré et est fonctionnel
L'API a bien été pris en compte
la commande pour build est 

" sudo docker build -t fastapi"
et pour lancé le conteneur utilisé la commande suivant 

"sudo docker run -d -e GROQ_API_KEY=votre clé API -p 5000:5000 fastapi"
![Screenshot from 2024-09-27 15-11-27](https://github.com/user-attachments/assets/55df71ac-570d-41ba-a0e6-96184602c69d)


dans le docker-compose.yml il lance un le service en https attention il faut généré un certificat
dont voice la capture d'ecran
![Screenshot from 2024-09-27 15-23-13](https://github.com/user-attachments/assets/8a0ddb3b-0da9-4686-900d-03c2512ef463)


## Repository github worflw
le processe d'automatisation de teste et d'envoie directement sur docker hub

![image](https://github.com/user-attachments/assets/ca06e2d1-e840-46b8-a0a8-fcc96e84d0d6)


![image](https://github.com/user-attachments/assets/072b4bc5-34f6-48dc-bc63-73f0d6471243)
