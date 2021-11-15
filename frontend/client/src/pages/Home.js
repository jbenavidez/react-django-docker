
import Services from '../components/Services';
import Portfolio  from '../components/Portfolio';
import About from '../components/About';
import Team from '../components/Team';
import Clients from '../components/Clients';

export default function Home() {
    return (
        <div>
        {/* Services  */}
        <section className="page-section" id="services">
           <Services/>
        </section>
        {/* Portfolio  */}
        <section  className="page-section bg-light" id="portfolio">
           <Portfolio/>
        </section>
         {/* About  */}
         <section   className="page-section" id="about">
           <About/>
        </section>
         {/* Team  */}
         <section    className="page-section bg-light" id="team">
           <Team/>
        </section>
         {/* Clients  */}
         <div className="py-5">
         <Clients/>
         </div>
     </div>
    )
}
