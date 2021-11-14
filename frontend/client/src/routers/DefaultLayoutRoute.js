
import React, { Component } from 'react';  
import { Route } from 'react-router-dom';  
import DefaultLayout from '../layouts/DefaultLayout'; 

export default function DefaultLayoutRoute({component: Component, ...rest}) {
    return (
        <Route {...rest} render={props => (  
            <DefaultLayout>  
                <Component {...props} />  
            </DefaultLayout>  
          )} /> 
    )
}
