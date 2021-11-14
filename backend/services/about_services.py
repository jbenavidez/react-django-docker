import logging 

logger = logging.getLogger(__name__)

class AboutServices:

    @classmethod
    def get_about_list(self):
        """this func return a list of services"""
        services_list =  [{
                    "name":" Humble Beginnings",
                    "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente, totam reiciendis temporibus qui quibusdam, recusandae sit vero unde, sed, incidunt et ea quo dolore laudantium consectetur!",
                    "img_url":"/img/about/1.jpg",
                    "date":"2009-2011",
                    "id":1,
                   
                    }, {
                    "name":"An Agency is Born",
                    "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente, totam reiciendis temporibus qui quibusdam, recusandae sit vero unde, sed, incidunt et ea quo dolore laudantium consectetur!",
                    "img_url":"/img/about/2.jpg",
                    "date":"March 2011",
                    "id":2,
                   
                    },{
                    "name":"Transition to Full Service",
                    "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente, totam reiciendis temporibus qui quibusdam, recusandae sit vero unde, sed, incidunt et ea quo dolore laudantium consectetur!",
                    "img_url":"/img/about/3.jpg",
                    "date":"December 2015",
                    "id":3,
                   
                    },{
                    "name":"Phase Two Expansion",
                    "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente, totam reiciendis temporibus qui quibusdam, recusandae sit vero unde, sed, incidunt et ea quo dolore laudantium consectetur!",
                    "img_url":"/img/about/4.jpg",
                    "date":"July 2020",
                    "id":4,
                   
                    }, 
                    
                ]
        return services_list