/* 
*  Copyright 2021 IBM Corporation
* 
*  Licensed under the Apache License, Version 2.0 (the "License"); 
*  you may not use this file except in compliance with the License. 
*  You may obtain a copy of the License at 
* 
*      http://www.apache.org/licenses/LICENSE-2.0 
* 
*  Unless required by applicable law or agreed to in writing, software 
*  distributed under the License is distributed on an "AS IS" BASIS, 
*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
*  See the License for the specific language governing permissions and 
*  limitations under the License. 
*/ 
import React, { useContext } from 'react';
import StoreContext from '../lib/stores/context'
import Hero from '../components/Hero'
import introPic from "../images/landing-page.png";
import { SET_ACTIVE_PAGE } from '../lib/stores/pages';
import Link from '../components/Link'
import PageFooter from '../components/PageFooter';
import Button from '../components/Button'

export default function LandingPage() {
  const { store, dispatch } = useContext(StoreContext)
  const { branding } = store.settings
  const { active } = store.pages

  const name = branding.name.value || branding.name.default

  if (active !== 'home')
    dispatch({ type: SET_ACTIVE_PAGE, page: 'home' })

  return (
    <div className="landing-page">
      <Hero
        title={name} 
        subtitle=" "
      >
      <Link to="https://github.com/machine-learning-exchange/mlx">
        <Button
          className="hero-buttons-outline"
          variant="outlined"
          color="primary"
        >
          Github
        </Button>
      </Link>
      </Hero>
      <div className="landing-page-wrapper">
        <h4 className="landing-page-text">
          Machine Learning eXchange (MLX) is an open source Data and AI assets catalog and execution engine, hosted in the 
          <Link to="https://lfaidata.foundation/"> LF AI & Data Foundation </Link>. 
          It allows the upload, registration, execution, and deployment of AI pipelines, pipeline components, models, datasets, and notebooks. 
          Please join our community on 
          <Link to="https://github.com/machine-learning-exchange"> Github </Link>!
        </h4>
        <img alt="MLX View" className="slide-img" src={introPic} />
      </div>
      <PageFooter/>
    </div>
  );
}
