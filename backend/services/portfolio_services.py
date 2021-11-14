

class PortfolioServices:

    @classmethod
    def get_portfolio_list(self):
        """this func return a portfolio  """
        portfolio_list =  [{
                    "name":"Threads",
                    "description":"Illustration",
                    "id":1,
                     "img_url":"/img/portfolio/1.jpg",
                    },{
                    "name":"Explore",
                    "description":"Graphic Design",
                    "id":2,
                     "img_url":"/img/portfolio/2.jpg",
                    },
                    {
                    "name":"Finish",
                    "description":"Identity",
                    "id":3,
                     "img_url":"/img/portfolio/3.jpg",
                    },
                    {
                    "name":"Lines",
                    "description":"Branding",
                    "id":4,
                     "img_url":"/img/portfolio/4.jpg",
                    }, {
                    "name":"Southwest",
                    "description":"Website Design",
                    "id":5,
                     "img_url":"/img/portfolio/5.jpg",
                    },
                     {
                    "name":"Window",
                    "product_description":"Photography",
                    "id":6,
                     "img_url":"/img/portfolio/6.jpg",
                    },
                  
                  
                ]
        return portfolio_list