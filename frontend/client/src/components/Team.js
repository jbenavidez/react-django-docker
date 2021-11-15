import useFetch from "../hooks/useFetch"

export default function Team() {
    const {data, isPending, error}= useFetch('/api/team/')
    return (
        <div>
            <div className="container">
                <div className="text-center">
                    <h2 className="section-heading text-uppercase">Our Amazing Team</h2>
                    <h3 className="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3>
                </div>
                <div className="row">
                    {!isPending  && 
                    <>
                    {
                    data.map((item , index) =>(
                    <div className="col-lg-4">
                        <div className="team-member"  key={index}>
                        <img className="mx-auto rounded-circle" src= { item.img_url}   alt="..." />
                        <h4>{ item.name} </h4>
                        <p className="text-muted">   { item.title} </p>
                        <a className="btn btn-dark btn-social mx-2" href="#!"><i className="fab fa-twitter"></i></a>
                        <a className="btn btn-dark btn-social mx-2" href="#!"><i className="fab fa-facebook-f"></i></a>
                        <a className="btn btn-dark btn-social mx-2" href="#!"><i className="fab fa-linkedin-in"></i></a>
                        </div>
                    </div>
                    ))
                    }
                    </>
                    }
                </div>
                <div className="row">
                    <div className="col-lg-8 mx-auto text-center">
                        <p className="large text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut eaque, laboriosam veritatis, quos non quis ad perspiciatis, totam corporis ea, alias ut unde.</p>
                    </div>
                </div>
            </div>
            </div>
    )
}
