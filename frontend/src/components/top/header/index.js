import style from "./style.css";

const Header = () => (
	<nav class={style.navbar} role="navigation" aria-label="main navigation">
		<div class="is-flex is-justify-content-space-between is-align-items-center">
			<div class="navbar-brand">
				<a class="navbar-item" href="/">
					<h1 class="is-size-3">3eets</h1>
				</a>
			</div>
			<div class="is-flex">
				
				<div class="buttons navbar-item are-small">
					<a href="/auth/login" class=" button is-primary">
						<strong>出品</strong>
					</a>
					<a href="/auth/login" class="button is-primary">
						<strong>ログイン</strong>
					</a>
				</div>
			</div>
		</div>
		<div class={style.navSearchPc}>
			<div class="control navbar-item">
				<input class="input" type="text" placeholder="search" />
			</div>
		</div>
	</nav>
);

export default Header;
