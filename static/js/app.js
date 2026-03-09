!(function (s) {
  "use strict";
  var e;
  function r() {
    for (
      var e = document
          .getElementById("topnav-menu-content")
          .getElementsByTagName("a"),
        t = 0,
        s = e.length;
      t < s;
      t++
    )
      "nav-item dropdown active" === e[t].parentElement.getAttribute("class") &&
        (e[t].parentElement.classList.remove("active"),
        null !== e[t].nextElementSibling &&
          e[t].nextElementSibling.classList.remove("show"));
  }

  function c(e) {
    const bootstrapCss = "{{ url_for('static', filename='assets/css/bootstrap.min.css') }}";
    const appCss = "{{ url_for('static', filename='assets/css/app.min.css') }}";
    const bootstrapRtlCss = "{{ url_for('static', filename='assets/css/bootstrap-rtl.min.css') }}";
    const appRtlCss = "{{ url_for('static', filename='assets/css/app-rtl.min.css') }}";

    1 == s("#light-mode-switch").prop("checked") && "light-mode-switch" === e
      ? (s("html").removeAttr("dir"),
        s("#dark-mode-switch").prop("checked", !1),
        s("#rtl-mode-switch").prop("checked", !1),
        s("#dark-rtl-mode-switch").prop("checked", !1),
        bootstrapCss != s("#bootstrap-style").attr("href") &&
          s("#bootstrap-style").attr("href", bootstrapCss),
        s("html").attr("data-bs-theme", "light"),
        appCss != s("#app-style").attr("href") &&
          s("#app-style").attr("href", appCss),
        sessionStorage.setItem("is_visited", "light-mode-switch"))
      : 1 == s("#dark-mode-switch").prop("checked") && "dark-mode-switch" === e
      ? (s("html").removeAttr("dir"),
        s("#light-mode-switch").prop("checked", !1),
        s("#rtl-mode-switch").prop("checked", !1),
        s("#dark-rtl-mode-switch").prop("checked", !1),
        s("html").attr("data-bs-theme", "dark"),
        bootstrapCss != s("#bootstrap-style").attr("href") &&
          s("#bootstrap-style").attr("href", bootstrapCss),
        appCss != s("#app-style").attr("href") &&
          s("#app-style").attr("href", appCss),
        sessionStorage.setItem("is_visited", "dark-mode-switch"))
      : 1 == s("#rtl-mode-switch").prop("checked") && "rtl-mode-switch" === e
      ? (s("#light-mode-switch").prop("checked", !1),
        s("#dark-mode-switch").prop("checked", !1),
        s("#dark-rtl-mode-switch").prop("checked", !1),
        bootstrapRtlCss != s("#bootstrap-style").attr("href") &&
          s("#bootstrap-style").attr("href", bootstrapRtlCss),
        appRtlCss != s("#app-style").attr("href") &&
          s("#app-style").attr("href", appRtlCss),
        s("html").attr("dir", "rtl"),
        s("html").attr("data-bs-theme", "light"),
        sessionStorage.setItem("is_visited", "rtl-mode-switch"))
      : 1 == s("#dark-rtl-mode-switch").prop("checked") &&
        "dark-rtl-mode-switch" === e &&
        (s("#light-mode-switch").prop("checked", !1),
        s("#rtl-mode-switch").prop("checked", !1),
        s("#dark-mode-switch").prop("checked", !1),
        bootstrapRtlCss != s("#bootstrap-style").attr("href") &&
          s("#bootstrap-style").attr("href", bootstrapRtlCss),
        appRtlCss != s("#app-style").attr("href") &&
          s("#app-style").attr("href", appRtlCss),
        s("html").attr("dir", "rtl"),
        s("html").attr("data-bs-theme", "dark"),
        sessionStorage.setItem("is_visited", "dark-rtl-mode-switch"));
  }

  function l() {
    document.webkitIsFullScreen ||
      document.mozFullScreen ||
      document.msFullscreenElement ||
      (console.log("pressed"), s("body").removeClass("fullscreen-enable"));
  }

  (s("#side-menu").metisMenu(),
    s("#vertical-menu-btn").on("click", function (e) {
      (e.preventDefault(),
        s("body").toggleClass("sidebar-enable"),
        992 <= s(window).width()
          ? s("body").toggleClass("vertical-collpsed")
          : s("body").removeClass("vertical-collpsed"));
    }),

    s("#sidebar-menu a").each(function () {
      var e = window.location.href.split(/[?#]/)[0];
      this.href == e &&
        (s(this).addClass("active"),
        s(this).parent().addClass("mm-active"),
        s(this).parent().parent().addClass("mm-show"),
        s(this).parent().parent().prev().addClass("mm-active"),
        s(this).parent().parent().parent().addClass("mm-active"),
        s(this).parent().parent().parent().parent().addClass("mm-show"),
        s(this)
          .parent()
          .parent()
          .parent()
          .parent()
          .parent()
          .addClass("mm-active"));
    }),

    s(document).ready(function () {
      var e;
      0 < s("#sidebar-menu").length &&
        0 < s("#sidebar-menu .mm-active .active").length &&
        300 < (e = s("#sidebar-menu .mm-active .active").offset().top) &&
        ((e -= 300),
        s(".vertical-menu .simplebar-content-wrapper").animate(
          { scrollTop: e },
          "slow",
        ));
    }),

    s(".navbar-nav a").each(function () {
      var e = window.location.href.split(/[?#]/)[0];
      this.href == e &&
        (s(this).addClass("active"),
        s(this).parent().addClass("active"),
        s(this).parent().parent().addClass("active"),
        s(this).parent().parent().parent().addClass("active"),
        s(this).parent().parent().parent().parent().addClass("active"),
        s(this).parent().parent().parent().parent().parent().addClass("active"),
        s(this)
          .parent()
          .parent()
          .parent()
          .parent()
          .parent()
          .parent()
          .addClass("active"));
    }),

    s('[data-bs-toggle="fullscreen"]').on("click", function (e) {
      (e.preventDefault(),
        s("body").toggleClass("fullscreen-enable"),
        document.fullscreenElement ||
        document.mozFullScreenElement ||
        document.webkitFullscreenElement
          ? document.cancelFullScreen
            ? document.cancelFullScreen()
            : document.mozCancelFullScreen
            ? document.mozCancelFullScreen()
            : document.webkitCancelFullScreen &&
              document.webkitCancelFullScreen()
          : document.documentElement.requestFullscreen
          ? document.documentElement.requestFullscreen()
          : document.documentElement.mozRequestFullScreen
          ? document.documentElement.mozRequestFullScreen()
          : document.documentElement.webkitRequestFullscreen &&
            document.documentElement.webkitRequestFullscreen(
              Element.ALLOW_KEYBOARD_INPUT,
            ));
    }),

    document.addEventListener("fullscreenchange", l),
    document.addEventListener("webkitfullscreenchange", l),
    document.addEventListener("mozfullscreenchange", l),

    s(".right-bar-toggle").on("click", function () {
      s("body").toggleClass("right-bar-enabled");
    }),

    s(document).on("click", "body", function (e) {
      0 < s(e.target).closest(".right-bar-toggle, .right-bar").length ||
        s("body").removeClass("right-bar-enabled");
    }),

    [].slice
      .call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
      .map(function (e) {
        return new bootstrap.Tooltip(e);
      }),

    [].slice
      .call(document.querySelectorAll('[data-bs-toggle="popover"]'))
      .map(function (e) {
        return new bootstrap.Popover(e);
      }),

    [].slice.call(document.querySelectorAll(".offcanvas")).map(function (e) {
      return new bootstrap.Offcanvas(e);
    }),

    s("#password-addon").on("click", function () {
      0 < s(this).siblings("input").length &&
        ("password" == s(this).siblings("input").attr("type")
          ? s(this).siblings("input").attr("type", "input")
          : s(this).siblings("input").attr("type", "password"));
    }),

    s(window).on("load", function () {
      (s("#status").fadeOut(), s("#preloader").delay(350).fadeOut("slow"));
    }),

    Waves.init(),

    s("#checkAll").on("change", function () {
      s(".table-check .form-check-input").prop(
        "checked",
        s(this).prop("checked"),
      );
    }),

    s(".table-check .form-check-input").change(function () {
      s(".table-check .form-check-input:checked").length ==
      s(".table-check .form-check-input").length
        ? s("#checkAll").prop("checked", !0)
        : s("#checkAll").prop("checked", !1);
    }));
})(jQuery);