import { h } from 'preact';
import {useEffect, useState} from "preact/hooks";
import "bulma/css/bulma.min.css";
import "./style.css";
import { Card, Button} from "preact-bulma";
import style from	"./style.css";

// Note: `user` comes from the URL, courtesy of our router
const Login = ({ user }) => {
	const [time, setTime] = useState(Date.now());
	const [count, setCount] = useState(10);

	useEffect(() => {
		let timer = setInterval(() => setTime(Date.now()), 1000);
		return () => clearInterval(timer);
	}, []);

	return (
		<div class={style.login}>
			<Card.Card>
				<Card.Header
					title="Log in"
					icon="fas fa-exclamation-circle"
				/>
				<Card.Content>
					<label>id:</label>
					<input name = "id" type="text" />
				</Card.Content>
				<Card.Content>
					<label>password:</label>
					<input name = "id" type="password" />
				</Card.Content>
				<Card.Footer>
					<Button>login</Button> 
				</Card.Footer>
			</Card.Card>
		</div>
	);
}

export default Login;
