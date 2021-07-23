import style from "./style.css";
const Header = () => (
	<nav class={style.navbar} role="navigation" aria-label="main navigation">
		<div class="navbar-brand">
			<a class="navbar-item" href="/">
				<h1 class="is-size-4">3eets Service</h1>
			</a>
		</div>
		<div class="navbar-end">
			<div class="navbar-item">
				<a href="/auth/login" class="button is-primary is-small">
					<strong>ログイン</strong>
				</a>
			</div>
		</div>
	</nav>
);

export default Header;
