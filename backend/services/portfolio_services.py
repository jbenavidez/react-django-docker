

class PortfolioServices:

    @classmethod
    def get_portfolio_list(self):
        """this func return a portfolio  """
        portfolio_list =  [{
                    "name":"Threads",
                    "description":"Illustration",
                 
                    "img_url":"/img/portfolio/1.jpg",
                    "id":1,
                    },{
                    "name":"Explore",
                    "description":"Graphic Design",                   
                     "img_url":"/img/portfolio/2.jpg",
                     "id":2,
                    },
                    {
                    "name":"Finish",
                    "description":"Identity",                  
                     "img_url":"/img/portfolio/3.jpg",
                      "id":3,
                    },
                    {
                    "name":"Lines",
                    "description":"Branding",                   
                     "img_url":"/img/portfolio/4.jpg",
                      "id":4,
                    }, {
                    "name":"Southwest",
                    "description":"Website Design",                   
                     "img_url":"/img/portfolio/5.jpg",
                     "id":5,
                    },
                     {
                    "name":"Window",
                    "product_description":"Photography",
                     "img_url":"/img/portfolio/6.jpg",
                     "id":6,
                    },
                  
                  
                ]
        return portfolio_list