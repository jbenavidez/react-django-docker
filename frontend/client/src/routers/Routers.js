
import React, { Component } from 'react';  
import { BrowserRouter as Router, Route, Switch ,  Redirect} from 'react-router-dom'
import DefaultLayoutRoute from './DefaultLayoutRoute';
import Home from '../pages/Home'



export default function Routers() {
    return (
        <div>
           <Router>
                <Switch>
                <Route exact path="/"><Redirect to="/home" /></Route>  
                <DefaultLayoutRoute  exact path="/home" component={Home} />
                </Switch>
            </Router>     
        </div>
    )
}
