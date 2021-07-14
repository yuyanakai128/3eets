import Router from 'preact-router';
import Register from './auth/register';
import Login from './auth/login';
import Password from './auth/password';
import TopDashBorad from './top/dashboard';
import Home from './users/home';

const routes = () => (
	<div>	
		<Router>
			<TopDashBorad path="/"/>
			<Login path="/auth/login" />
			<Register path="/auth/register" />
			<Password path="/auth/password" />
			<Home path="/users/home" />
		</Router>
	</div>
);

export default routes;