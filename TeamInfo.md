# Team038-Random_group_2

## Basic Information

|   Info      |        Description     |
| ----------- | ---------------------- |
| TeamID      |         Team-038       |
| TeamName    |     Random_group_2     |
| Captain     |      Matthew Ding      |
| Captain     |  mding9@illinois.edu   |
| Member1     |       Wonjun Cho       |
| Member1     |  wonjun2@illinois.edu  |
| Member2     |     Nandana Dileep     |
| Member2     | kdileep2@illinois.edu  |

## Project Information

|   Info      |        Description     |
| ----------- | ---------------------- |
|  Title      |       ProjectTitle     |
| System URL  |      link_to_system    |
| Video Link  |      link_to_video     |

## Project Summary
  Our application will be used to compile apartments and dorms for students looking for lodging at UIUC. There will be 4 tables, offers, tracked offers, users, and providers. The Offers table will have attributes including the name of the person providing the offer, location, rent cost, start date, end date, cancel date, whether it can be subleased, and what utilities are provided. The utilities will be gas, electricity, water, and internet. The utilities will be listed as their costs, where they are 0 if they are provided with the lease, equal to the cost if they are provided separately, and -1 if you have to provide your own. The Tracked Offers table will have a foreign key referencing the Offers table’s ID, and will have additional attributes related to communication to the offer provider.
Another table or function might be required to calculate distances from important locations, like the engineering quad or undergraduate library.
The Provider table will have information (name, email address, phone number) about who is offering the room and which room they are offering. 
The User table, you will find information (name, email address, phone number)  about the customer who wants to use the room and which room they have reserved.

