import logging 

logger = logging.getLogger(__name__)

class TeamServices:

    @classmethod
    def get_team_list(self):
        """this func return a list team member"""
        services_list =  [{
                    "name":"Parveen Anand",
                    "title":"Lead Designer",
                    "img_url":"/img/team/1.jpg",
                    "id":1,
                   
                    },{
                    "name":"Diana Petersen",
                    "title":"Lead Marketer",
                      "img_url":"/img/team/2.jpg",
                    "id":2,
                   
                    },
                    {
                    "name":"Larry Parker",
                    "title":"Lead Developer",
                    "img_url":"/img/team/3.jpg",
                    "id":3,
                     
                    },
                    
                ]
        return services_list