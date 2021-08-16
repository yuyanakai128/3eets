import { useState } from 'preact/hooks';
import style from "./style.css";


const Common = (props) => {
  const [active, setActive] = useState(1);
  const [second, setSecond] = useState(1);
	return (
    <>
      <ul class={style.type}>
        <li class={style.label}>種類：</li>
        <li class={style.button}>同種</li>
        <li class={style.button}>異種</li>
        <li class={style.button}>指定なし</li>
        <li class={style.label}></li>
      </ul>
      <ul class={style.method}>
        <li class={style.label}>方法：</li>
        <li class={style.button}>手渡し</li>
        <li class={style.button}>郵送</li>
        <li class={style.button}>追跡付き</li>
        <li class={style.button}>指定なし</li>
      </ul>
    </>
  );
}

export default Common;
