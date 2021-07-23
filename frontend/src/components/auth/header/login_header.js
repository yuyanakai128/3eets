import style from "./style.css";
const LoginHeader = () => (
	<nav class={style.navbar} role="navigation" aria-label="main navigation">
		<div class="navbar-brand">
			<a class="navbar-item" href="/">
				<h1 class="is-size-4">3eets Service</h1>
			</a>
		</div>
	</nav>
);

export default LoginHeader;
