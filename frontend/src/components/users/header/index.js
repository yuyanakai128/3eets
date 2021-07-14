import style from "./style.css";

const Header = () => (
	<nav class={style.navbar} role="navigation" aria-label="main navigation">
		<div class="is-flex is-justify-content-space-between is-align-items-center">
			<div class="navbar-brand">
				<a class="navbar-item" href="/">
					<h1 class="is-size-4">SERVICENAME</h1>
				</a>
			</div>
			<div class="is-flex">
				<div class={style.navSearchPc}>
					<div class="control navbar-item">
						<input class="input" type="text" placeholder="search" />
					</div>
				</div>
				<div class="buttons navbar-item are-small">
					<a href="/" class="button is-primary">
						<strong>ログアウト</strong>
					</a>
				</div>
			</div>
		</div>
		
	
		<div class={style.navSearchSp}>
			<div class="control navbar-item">
				<input class="input" type="text" placeholder="search" />
			</div>
		</div>
	</nav>
);

export default Header;
