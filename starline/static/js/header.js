window.addEventListener('DOMContentLoaded', (event) => {

    //! функция headerSticky для fixed header и появления новых блоков!

    window.addEventListener('scroll', headerSticky);

    const header = document.querySelector('.header-wrap'),
        mainWrap = document.querySelector('.main-wrap'),
        logoHeader = document.querySelector('.logo-desktop'),
        socialHeader = document.querySelector('.header__contact-mob'),
        mainContent = document.querySelector('.main');

    let sticky = header.offsetTop;

    function headerSticky() {
        if(window.innerWidth > 768){
            if (window.pageYOffset >= sticky) {
                mainWrap.classList.add('content');
                header.classList.add('sticky');
                logoHeader.classList.add('fade');
                socialHeader.classList.add('fade');
                mainContent.classList.add('header-active');
            } else {
                mainWrap.classList.remove('content');
                header.classList.remove('sticky');
                logoHeader.classList.remove('fade');
                socialHeader.classList.remove('fade');
                mainContent.classList.remove('header-active');
            }
        }
    }

    //!  функция menuActive для отображения menu

    const menuBurger = document.querySelector('.header__burger');
        menuBurger.addEventListener('click', menuActive);

    function menuActive(){
        const menuNav = document.querySelector('.header__menu');

        let vh = window.innerHeight * 0.01;

        document.documentElement.style.setProperty('--vh', `${vh}px`);
        menuNav.classList.toggle('active');
        menuBurger.classList.toggle('active');
        document.body.classList.toggle('body-h');
    }
})
