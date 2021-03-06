$(document).ready(function () {
    template_functions();
    init_masonry();
    charts();
    calendars();
    growlLikeNotifications();
    widthFunctions();
    if (jQuery.browser.version.substring(0, 2) == "8.") {
    } else {
        circle_progess()
    }
    messageLike();
    setInterval(tempStats, 3000)
});

function messageLike() {
    if ($(".messagesList")) {
        $(".messagesList").on("click", ".star", function () {
            $(this).removeClass("star");
            $(this).addClass("dislikes")
        });
        $(".messagesList").on("click", ".dislikes", function () {
            $(this).removeClass("dislikes");
            $(this).addClass("star")
        })
    }
}

function tempStats() {
    if ($(".tempStat")) {
        $(".tempStat").each(function () {
            var a = Math.floor(Math.random() * (1 + 120));
            $(this).html(a + "Â°");
            if (a < 20) {
                $(this).animate({borderColor: "#67c2ef"}, "fast")
            } else {
                if (a > 19 && a < 40) {
                    $(this).animate({borderColor: "#CBE968"}, "slow")
                } else {
                    if (a > 39 && a < 60) {
                        $(this).animate({borderColor: "#eae874"}, "slow")
                    } else {
                        if (a > 59 && a < 80) {
                            $(this).animate({borderColor: "#fabb3d"}, "slow")
                        } else {
                            if (a > 79 && a < 100) {
                                $(this).animate({borderColor: "#fa603d"}, "slow")
                            } else {
                                $(this).animate({borderColor: "#ff5454"}, "slow")
                            }
                        }
                    }
                }
            }
        })
    }
}

function init_masonry() {
    var b = $(".masonry-gallery");
    var a = 6;
    var c = 250;
    b.imagesLoaded(function () {
        b.masonry({
            itemSelector: ".masonry-thumb", gutterWidth: a, isAnimated: true, columnWidth: function (e) {
                var d = (e / c | 0);
                var f = (((e - (d - 1) * a) / d) | 0);
                if (e < c) {
                    f = e
                }
                $(".masonry-thumb").width(f);
                return f
            }
        })
    })
}

function numberWithCommas(a) {
    a = a.toString();
    var b = /(-?\d+)(\d{3})/;
    while (b.test(a)) {
        a = a.replace(b, "$1.$2")
    }
    return a
}

function template_functions() {
    if ($("#g1").length) {
        g1 = new JustGage({id: "g1", value: 67, min: 0, max: 100, title: "Visitors", label: "per minute"});
        g1a = new JustGage({id: "g1a", value: 45, min: 0, max: 100, title: "Errors", label: "average"});
        g2 = new JustGage({id: "g2", value: 15, min: 0, max: 100, title: "Timers", label: ""});
        g2a = new JustGage({id: "g2a", value: 7, min: 0, max: 100, title: "Alerts", label: ""});
        g2b = new JustGage({id: "g2b", value: 22, min: 0, max: 100, title: "Events", label: ""});
        setInterval(function () {
            g1.refresh(getRandomInt(50, 100));
            g1a.refresh(getRandomInt(50, 100));
            g2.refresh(getRandomInt(0, 50));
            g2a.refresh(getRandomInt(0, 50));
            g2b.refresh(getRandomInt(0, 50))
        }, 2000)
    } else {
    }
    $("#myWizard").wizard();
    $('a[href="#"][data-top!=true]').click(function (b) {
        b.preventDefault()
    });
    $(".cleditor").cleditor();
    $(".datepicker").datepicker();
    $(".noty").click(function (c) {
        c.preventDefault();
        var b = $.parseJSON($(this).attr("data-noty-options"));
        noty(b)
    });
    $("input:checkbox, input:radio, input:file").not('[data-no-uniform="true"],#uniform-is-ajax').uniform();
    $('[data-rel="chosen"],[rel="chosen"]').chosen();
    $("#myTab a:first").tab("show");
    $("#myTab a").click(function (b) {
        b.preventDefault();
        $(this).tab("show")
    });
    $(".sortable").sortable({
        revert: true, cancel: ".btn,.box-content,.nav-header", update: function (b, c) {
        }
    });
    $('[rel="tooltip"],[data-rel="tooltip"]').tooltip({placement: "bottom", delay: {show: 400, hide: 200}});
    $('[rel="popover"],[data-rel="popover"]').popover();
    var a = $(".file-manager").elfinder({url: "misc/elfinder-connector/connector.php"}).elfinder("instance");
    $(".raty").raty({score: 4});
    $("#file_upload").uploadify({swf: "misc/uploadify.swf", uploader: "misc/uploadify.php"});
    $("#toggle-fullscreen").button().click(function () {
        var c = $(this), b = document.documentElement;
        if (!c.hasClass("active")) {
            $("#thumbnails").addClass("modal-fullscreen");
            if (b.webkitRequestFullScreen) {
                b.webkitRequestFullScreen(window.Element.ALLOW_KEYBOARD_INPUT)
            } else {
                if (b.mozRequestFullScreen) {
                    b.mozRequestFullScreen()
                }
            }
        } else {
            $("#thumbnails").removeClass("modal-fullscreen");
            (document.webkitCancelFullScreen || document.mozCancelFullScreen || $.noop).apply(document)
        }
    });
    $(".datatable").dataTable({
        sDom: "<'row-fluid'<'span6'l><'span6'f>r>t<'row-fluid'<'span12'i><'span12 center'p>>",
        sPaginationType: "bootstrap",
        oLanguage: {sLengthMenu: "_MENU_ records per page"}
    });
    $(".btn-close").click(function (b) {
        b.preventDefault();
        $(this).parent().parent().parent().fadeOut()
    });
    $(".btn-minimize").click(function (c) {
        c.preventDefault();
        var b = $(this).parent().parent().next(".box-content");
        if (b.is(":visible")) {
            $("i", $(this)).removeClass("icon-chevron-up").addClass("icon-chevron-down")
        } else {
            $("i", $(this)).removeClass("icon-chevron-down").addClass("icon-chevron-up")
        }
        b.slideToggle()
    });
    $(".btn-setting").click(function (b) {
        b.preventDefault();
        $("#myModal").modal("show")
    });
    $(".simpleProgress").progressbar({value: 89});
    $(".progressAnimate").progressbar({
        value: 1, create: function () {
            $(".progressAnimate .ui-progressbar-value").animate({width: "100%"}, {
                duration: 10000, step: function (b) {
                    $(".progressAnimateValue").html(parseInt(b) + "%")
                }, easing: "linear"
            })
        }
    });
    $(".progressUploadAnimate").progressbar({
        value: 1, create: function () {
            $(".progressUploadAnimate .ui-progressbar-value").animate({width: "100%"}, {
                duration: 20000,
                easing: "linear",
                step: function (b) {
                    $(".progressUploadAnimateValue").html(parseInt(b * 40.96) + " Gb")
                },
                complete: function () {
                    $(".progressUploadAnimate + .field_notice").html("<span class='must'>Upload Finished</span>")
                }
            })
        }
    });
    if ($(".taskProgress")) {
        $(".taskProgress").each(function () {
            var b = parseInt($(this).html());
            $(this).progressbar({value: b});
            $(this).parent().find(".percent").html(b + "%")
        })
    }
    if ($(".progressBarValue")) {
        $(".progressBarValue").each(function () {
            var c = $(this).find(".progressCustomValueVal").html();
            var b = parseInt(c);
            $(this).find(".progressCustomValue").progressbar({
                value: 1, create: function () {
                    $(this).find(".ui-progressbar-value").animate({width: b + "%"}, {
                        duration: 5000,
                        step: function (d) {
                            $(this).parent().parent().parent().find(".progressCustomValueVal").html(parseInt(d) + "%")
                        },
                        easing: "linear"
                    })
                }
            })
        })
    }
    $(".sliderSimple").slider();
    $(".sliderMin").slider({
        range: "min", value: 180, min: 1, max: 700, slide: function (b, c) {
            $(".sliderMinLabel").html("$" + c.value)
        }
    });
    $(".sliderMin-1").slider({
        range: "min", value: 50, min: 1, max: 700, slide: function (b, c) {
            $(".sliderMin1Label").html("$" + c.value)
        }
    });
    $(".sliderMin-2").slider({
        range: "min", value: 100, min: 1, max: 700, slide: function (b, c) {
            $(".sliderMin2Label").html("$" + c.value)
        }
    });
    $(".sliderMin-3").slider({
        range: "min", value: 150, min: 1, max: 700, slide: function (b, c) {
            $(".sliderMin3Label").html("$" + c.value)
        }
    });
    $(".sliderMin-4").slider({
        range: "min", value: 250, min: 1, max: 700, slide: function (b, c) {
            $(".sliderMin4Label").html("$" + c.value)
        }
    });
    $(".sliderMin-5").slider({
        range: "min", value: 350, min: 1, max: 700, slide: function (b, c) {
            $(".sliderLabel").html("$" + c.value)
        }
    });
    $(".sliderMin-6").slider({
        range: "min", value: 450, min: 1, max: 700, slide: function (b, c) {
            $(".sliderLabel").html("$" + c.value)
        }
    });
    $(".sliderMin-7").slider({
        range: "min", value: 550, min: 1, max: 700, slide: function (b, c) {
            $(".sliderLabel").html("$" + c.value)
        }
    });
    $(".sliderMin-8").slider({
        range: "min", value: 650, min: 1, max: 700, slide: function (b, c) {
            $(".sliderLabel").html("$" + c.value)
        }
    });
    $(".sliderMax").slider({
        range: "max", value: 280, min: 1, max: 700, slide: function (b, c) {
            $(".sliderMaxLabel").html("$" + c.value)
        }
    });
    $(".sliderRange").slider({
        range: true, min: 0, max: 500, values: [192, 470], slide: function (b, c) {
            $(".sliderRangeLabel").html("$" + c.values[0] + " - $" + c.values[1])
        }
    });
    $("#sliderVertical-1").slider({orientation: "vertical", range: "min", min: 0, max: 100, value: 60});
    $("#sliderVertical-2").slider({orientation: "vertical", range: "min", min: 0, max: 100, value: 40});
    $("#sliderVertical-3").slider({orientation: "vertical", range: "min", min: 0, max: 100, value: 30});
    $("#sliderVertical-4").slider({orientation: "vertical", range: "min", min: 0, max: 100, value: 15});
    $("#sliderVertical-5").slider({orientation: "vertical", range: "min", min: 0, max: 100, value: 40});
    $("#sliderVertical-6").slider({orientation: "vertical", range: "min", min: 0, max: 100, value: 80});
    $("#sliderVertical-7").slider({orientation: "vertical", range: "min", min: 0, max: 100, value: 60});
    $("#sliderVertical-8").slider({orientation: "vertical", range: "min", min: 0, max: 100, value: 40});
    $("#sliderVertical-9").slider({orientation: "vertical", range: "min", min: 0, max: 100, value: 30});
    $("#sliderVertical-10").slider({orientation: "vertical", range: "min", min: 0, max: 100, value: 15});
    $("#sliderVertical-11").slider({orientation: "vertical", range: "min", min: 0, max: 100, value: 40});
    $("#sliderVertical-12").slider({orientation: "vertical", range: "min", min: 0, max: 100, value: 80})
}

function circle_progess() {
    var a = $("div");
    if (retina()) {
        $(".whiteCircle").knob({
            min: 0,
            max: 100,
            readOnly: true,
            width: 240,
            height: 240,
            bgColor: "rgba(255,255,255,0.5)",
            fgColor: "rgba(255,255,255,0.9)",
            dynamicDraw: true,
            thickness: 0.2,
            tickColorizeValues: true
        });
        $(".circleStat").css("zoom", 0.5);
        $(".whiteCircle").css("zoom", 0.999)
    } else {
        $(".whiteCircle").knob({
            min: 0,
            max: 100,
            readOnly: true,
            width: 120,
            height: 120,
            bgColor: "rgba(255,255,255,0.5)",
            fgColor: "rgba(255,255,255,0.9)",
            dynamicDraw: true,
            thickness: 0.2,
            tickColorizeValues: true
        })
    }
    $(".circleStatsItemBox").each(function () {
        var d = $(this).find(".value > .number").html();
        var c = $(this).find(".value > .unit").html();
        var b = $(this).find("input").val() / 100;
        countSpeed = 2300 * b;
        endValue = d * b;
        $(this).find(".count > .unit").html(c);
        $(this).find(".count > .number").countTo({
            from: 0,
            to: endValue,
            speed: countSpeed,
            refreshInterval: 50,
            onComplete: function (e) {
                console.debug(this)
            }
        })
    });
    $(".circleChart").each(function () {
        var b = $(this).parent().css("color");
        $(this).knob({
            min: 0,
            max: 100,
            readOnly: true,
            width: 120,
            height: 120,
            fgColor: b,
            dynamicDraw: true,
            thickness: 0.2,
            tickColorizeValues: true,
            skin: "tron"
        })
    });
    $(".knob").each(function () {
        $(this).knob()
    })
}

function calendars() {
    $("#external-events div.external-event").each(function () {
        var d = {title: $.trim($(this).text())};
        $(this).data("eventObject", d);
        $(this).draggable({zIndex: 999, revert: true, revertDuration: 0})
    });
    var b = new Date();
    var c = b.getDate();
    var a = b.getMonth();
    var e = b.getFullYear();
    $("#main_calendar").fullCalendar({
        header: {left: "title", right: "prev,next today,month,agendaWeek,agendaDay"},
        editable: true,
        events: [{title: "All Day Event", start: new Date(e, a, 1)}, {
            title: "Long Event",
            start: new Date(e, a, c - 5),
            end: new Date(e, a, c - 2)
        }, {id: 999, title: "Repeating Event", start: new Date(e, a, c - 3, 16, 0), allDay: false}, {
            id: 999,
            title: "Repeating Event",
            start: new Date(e, a, c + 4, 16, 0),
            allDay: false
        }, {title: "Meeting", start: new Date(e, a, c, 10, 30), allDay: false}, {
            title: "Lunch",
            start: new Date(e, a, c, 12, 0),
            end: new Date(e, a, c, 14, 0),
            allDay: false
        }, {
            title: "Birthday Party",
            start: new Date(e, a, c + 1, 19, 0),
            end: new Date(e, a, c + 1, 22, 30),
            allDay: false
        }, {title: "Click for Google", start: new Date(e, a, 28), end: new Date(e, a, 29), url: "http://google.com/"}]
    });
    $(".calendar-small").fullCalendar({
        header: {right: "title", left: "prev,next,today"},
        defaultView: "month",
        editable: true,
        events: [{
            title: "All Day Event",
            start: new Date(b.getFullYear(), b.getMonth(), b.getDate() - 17),
            allDay: true
        }, {
            title: "Long Event",
            start: new Date(b.getFullYear(), b.getMonth(), b.getDate() - 15, 11, 30, 0),
            end: new Date(b.getFullYear(), b.getMonth(), b.getDate() - 10, 12, 30, 0)
        }, {
            id: 999,
            title: "Repeating Event",
            start: new Date(b.getFullYear(), b.getMonth(), b.getDate() - 9, 8, 0, 0),
            end: new Date(b.getFullYear(), b.getMonth(), b.getDate() - 9, 10, 0, 0),
            allDay: false
        }, {
            id: 999,
            title: "Repeating Event",
            start: new Date(b.getFullYear(), b.getMonth(), b.getDate() - 2, 8, 0, 0),
            end: new Date(b.getFullYear(), b.getMonth(), b.getDate() - 2, 10, 0, 0),
            allDay: false
        }, {
            title: "Meeting",
            start: new Date(b.getFullYear(), b.getMonth(), b.getDate(), 11, 30, 0),
            end: new Date(b.getFullYear(), b.getMonth(), b.getDate(), 12, 30, 0),
            allDay: false
        }, {
            title: "Lunch",
            start: new Date(b.getFullYear(), b.getMonth(), b.getDate(), 14, 0, 0),
            end: new Date(b.getFullYear(), b.getMonth(), b.getDate(), 15, 30, 0),
            allDay: false
        }, {
            title: "Birthday Party",
            start: new Date(b.getFullYear(), b.getMonth(), b.getDate() + 1, 19, 30, 0),
            end: new Date(b.getFullYear(), b.getMonth(), b.getDate() + 1, 22, 30, 0),
            allDay: false
        }, {
            title: "Click for Google",
            start: new Date(b.getFullYear(), b.getMonth(), b.getDate() + 10, 14, 30, 0),
            end: new Date(b.getFullYear(), b.getMonth(), b.getDate() + 11, 12, 30, 0),
            url: "http://google.com/"
        }],
        dayClick: function (g, j, f, d) {
            $(".calendar-details > .events").html("");
            var i = new Array(7);
            i[0] = "Sunday";
            i[1] = "Monday";
            i[2] = "Tuesday";
            i[3] = "Wednesday";
            i[4] = "Thursday";
            i[5] = "Friday";
            i[6] = "Saturday";
            var k = new Array();
            k[0] = "January";
            k[1] = "February";
            k[2] = "March";
            k[3] = "April";
            k[4] = "May";
            k[5] = "June";
            k[6] = "July";
            k[7] = "August";
            k[8] = "September";
            k[9] = "October";
            k[10] = "November";
            k[11] = "December";
            var h = new Date(g.getFullYear(), g.getMonth(), g.getDate() + 1);
            var l = $(".calendar-small").fullCalendar("clientEvents", function (n) {
                function o(r) {
                    return r < 10 ? "0" + r : r
                }

                if (n.start >= g && n.start < h) {
                    var p = n.title;
                    var q = n.start;
                    var m = n.end;
                    $(".calendar-details > .day").html(i[g.getDay()]);
                    $(".calendar-details > .date").html(k[g.getMonth()] + " " + g.getDate());
                    if (n.allDay) {
                        $(".calendar-details > .events").append("<li>" + p + " - all day</li>")
                    } else {
                        $(".calendar-details > .events").append("<li>" + p + " - " + q.getHours() + ":" + o(q.getMinutes()) + " - " + m.getHours() + ":" + o(m.getMinutes()) + "</li>")
                    }
                } else {
                    if (g >= n.start && g <= n.end) {
                        var p = n.title;
                        var q = n.start;
                        var m = n.end;
                        $(".calendar-details > .day").html(i[g.getDay()]);
                        $(".calendar-details > .date").html(k[g.getMonth()] + " " + g.getDate());
                        $(".calendar-details > .events").append("<li>" + p + " - " + k[q.getMonth()] + " " + q.getDate() + " " + q.getHours() + ":" + o(q.getMinutes()) + " - " + k[m.getMonth()] + " " + m.getDate() + " " + m.getHours() + ":" + o(m.getMinutes()) + "</li>")
                    } else {
                        $(".calendar-details > .day").html(i[g.getDay()]);
                        $(".calendar-details > .date").html(k[g.getMonth()] + " " + g.getDate())
                    }
                }
            });
            if ($(".calendar-details ul li").length == 0) {
                $(".calendar-details > .events").html("<li>no events :)</li>")
            }
        }
    });
    $("#main_calendar_phone").fullCalendar({
        header: {left: "title", right: "prev,next"},
        defaultView: "agendaDay",
        editable: true,
        events: [{title: "All Day Event", start: new Date(e, a, 1)}, {
            title: "Long Event",
            start: new Date(e, a, c - 5),
            end: new Date(e, a, c - 2)
        }, {id: 999, title: "Repeating Event", start: new Date(e, a, c - 3, 16, 0), allDay: false}, {
            id: 999,
            title: "Repeating Event",
            start: new Date(e, a, c + 4, 16, 0),
            allDay: false
        }, {title: "Meeting", start: new Date(e, a, c, 10, 30), allDay: false}, {
            title: "Lunch",
            start: new Date(e, a, c, 12, 0),
            end: new Date(e, a, c, 14, 0),
            allDay: false
        }, {
            title: "Birthday Party",
            start: new Date(e, a, c + 1, 19, 0),
            end: new Date(e, a, c + 1, 22, 30),
            allDay: false
        }, {title: "Click for Google", start: new Date(e, a, 28), end: new Date(e, a, 29), url: "http://google.com/"}]
    });
    $("#calendar").fullCalendar({
        header: {left: "title", right: "prev,next today,month,agendaWeek,agendaDay"},
        editable: true,
        droppable: true,
        drop: function (g, h) {
            var f = $(this).data("eventObject");
            var d = $.extend({}, f);
            d.start = g;
            d.allDay = h;
            $("#calendar").fullCalendar("renderEvent", d, true);
            if ($("#drop-remove").is(":checked")) {
                $(this).remove()
            }
        }
    })
}

function growlLikeNotifications() {
    $("#add-sticky").click(function () {
        var a = $.gritter.add({
            title: "This is a sticky notice!",
            text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget tincidunt velit. Cum sociis natoque penatibus et <a href="#" style="color:#ccc">magnis dis parturient</a> montes, nascetur ridiculus mus.',
            image: "img/avatar.jpg",
            sticky: true,
            time: "",
            class_name: "my-sticky-class"
        });
        return false
    });
    $("#add-regular").click(function () {
        $.gritter.add({
            title: "This is a regular notice!",
            text: 'This will fade out after a certain amount of time. Vivamus eget tincidunt velit. Cum sociis natoque penatibus et <a href="#" style="color:#ccc">magnis dis parturient</a> montes, nascetur ridiculus mus.',
            image: "img/avatar.jpg",
            sticky: false,
            time: ""
        });
        return false
    });
    $("#add-max").click(function () {
        $.gritter.add({
            title: "This is a notice with a max of 3 on screen at one time!",
            text: 'This will fade out after a certain amount of time. Vivamus eget tincidunt velit. Cum sociis natoque penatibus et <a href="#" style="color:#ccc">magnis dis parturient</a> montes, nascetur ridiculus mus.',
            image: "img/avatar.jpg",
            sticky: false,
            before_open: function () {
                if ($(".gritter-item-wrapper").length == 3) {
                    return false
                }
            }
        });
        return false
    });
    $("#add-without-image").click(function () {
        $.gritter.add({
            title: "This is a notice without an image!",
            text: 'This will fade out after a certain amount of time. Vivamus eget tincidunt velit. Cum sociis natoque penatibus et <a href="#" style="color:#ccc">magnis dis parturient</a> montes, nascetur ridiculus mus.'
        });
        return false
    });
    $("#add-gritter-light").click(function () {
        $.gritter.add({
            title: "This is a light notification",
            text: 'Just add a "gritter-light" class_name to your $.gritter.add or globally to $.gritter.options.class_name',
            class_name: "gritter-light"
        });
        return false
    });
    $("#add-with-callbacks").click(function () {
        $.gritter.add({
            title: "This is a notice with callbacks!", text: "The callback is...", before_open: function () {
                alert("I am called before it opens")
            }, after_open: function (a) {
                alert("I am called after it opens: \nI am passed the jQuery object for the created Gritter element...\n" + a)
            }, before_close: function (b, c) {
                var a = (c) ? 'The "X" was clicked to close me!' : "";
                alert("I am called before it closes: I am passed the jQuery object for the Gritter element... \n" + a)
            }, after_close: function (b, c) {
                var a = (c) ? 'The "X" was clicked to close me!' : "";
                alert("I am called after it closes. " + a)
            }
        });
        return false
    });
    $("#add-sticky-with-callbacks").click(function () {
        $.gritter.add({
            title: "This is a sticky notice with callbacks!",
            text: "Sticky sticky notice.. sticky sticky notice...",
            sticky: true,
            before_open: function () {
                alert("I am a sticky called before it opens")
            },
            after_open: function (a) {
                alert("I am a sticky called after it opens: \nI am passed the jQuery object for the created Gritter element...\n" + a)
            },
            before_close: function (a) {
                alert("I am a sticky called before it closes: I am passed the jQuery object for the Gritter element... \n" + a)
            },
            after_close: function () {
                alert("I am a sticky called after it closes")
            }
        });
        return false
    });
    $("#remove-all").click(function () {
        $.gritter.removeAll();
        return false
    });
    $("#remove-all-with-callbacks").click(function () {
        $.gritter.removeAll({
            before_close: function (a) {
                alert("I am called before all notifications are closed.  I am passed the jQuery object containing all  of Gritter notifications.\n" + a)
            }, after_close: function () {
                alert("I am called after everything has been closed.")
            }
        });
        return false
    })
}

$.fn.dataTableExt.oApi.fnPagingInfo = function (a) {
    return {
        iStart: a._iDisplayStart,
        iEnd: a.fnDisplayEnd(),
        iLength: a._iDisplayLength,
        iTotal: a.fnRecordsTotal(),
        iFilteredTotal: a.fnRecordsDisplay(),
        iPage: Math.ceil(a._iDisplayStart / a._iDisplayLength),
        iTotalPages: Math.ceil(a.fnRecordsDisplay() / a._iDisplayLength)
    }
};
$.extend($.fn.dataTableExt.oPagination, {
    bootstrap: {
        fnInit: function (e, b, d) {
            var a = e.oLanguage.oPaginate;
            var f = function (g) {
                g.preventDefault();
                if (e.oApi._fnPageChange(e, g.data.action)) {
                    d(e)
                }
            };
            $(b).addClass("pagination").append('<ul><li class="prev disabled"><a href="#">&larr; ' + a.sPrevious + '</a></li><li class="next disabled"><a href="#">' + a.sNext + " &rarr; </a></li></ul>");
            var c = $("a", b);
            $(c[0]).bind("click.DT", {action: "previous"}, f);
            $(c[1]).bind("click.DT", {action: "next"}, f)
        }, fnUpdate: function (c, k) {
            var l = 5;
            var e = c.oInstance.fnPagingInfo();
            var h = c.aanFeatures.p;
            var g, f, d, a, m, b = Math.floor(l / 2);
            if (e.iTotalPages < l) {
                a = 1;
                m = e.iTotalPages
            } else {
                if (e.iPage <= b) {
                    a = 1;
                    m = l
                } else {
                    if (e.iPage >= (e.iTotalPages - b)) {
                        a = e.iTotalPages - l + 1;
                        m = e.iTotalPages
                    } else {
                        a = e.iPage - b + 1;
                        m = a + l - 1
                    }
                }
            }
            for (g = 0, iLen = h.length; g < iLen; g++) {
                $("li:gt(0)", h[g]).filter(":not(:last)").remove();
                for (f = a; f <= m; f++) {
                    d = (f == e.iPage + 1) ? 'class="active"' : "";
                    $("<li " + d + '><a href="#">' + f + "</a></li>").insertBefore($("li:last", h[g])[0]).bind("click", function (i) {
                        i.preventDefault();
                        c._iDisplayStart = (parseInt($("a", this).text(), 10) - 1) * e.iLength;
                        k(c)
                    })
                }
                if (e.iPage === 0) {
                    $("li:first", h[g]).addClass("disabled")
                } else {
                    $("li:first", h[g]).removeClass("disabled")
                }
                if (e.iPage === e.iTotalPages - 1 || e.iTotalPages === 0) {
                    $("li:last", h[g]).addClass("disabled")
                } else {
                    $("li:last", h[g]).removeClass("disabled")
                }
            }
        }
    }
});
$(window).bind("resize", widthFunctions);

function widthFunctions(g) {
    var d = $(".sidebar-nav").height() + 50;
    var c = $(window).height();
    var b = $(window).width();
    if (b > 767) {
        if (c - 80 > d) {
            var a = $("header").height();
            var f = $("footer").height();
            $("#content").css("min-height", c - 80)
        } else {
            $("#content").css("min-height", d)
        }
    }
    if (b < 980 && b > 767) {
        if ($(".main-menu-span").hasClass("span2")) {
            $(".main-menu-span").removeClass("span2");
            $(".main-menu-span").addClass("span1")
        }
        if ($(".brand").hasClass("span2")) {
            $(".brand").removeClass("span2");
            $(".brand").addClass("span1")
        }
        if ($("#content").hasClass("span10")) {
            $("#content").removeClass("span10");
            $("#content").addClass("span11")
        }
        $("a").each(function () {
            if ($(this).hasClass("quick-button-small span1")) {
                $(this).removeClass("quick-button-small span1");
                $(this).addClass("quick-button span2 changed")
            }
        });
        $(".circleStatsItem, .circleStatsItemBox").each(function () {
            var e = $(this).parent().attr("onTablet");
            var h = $(this).parent().attr("onDesktop");
            if (e) {
                $(this).parent().removeClass(h);
                $(this).parent().addClass(e)
            }
        });
        $(".tempStatBox").each(function () {
            var e = $(this).attr("onTablet");
            var h = $(this).attr("onDesktop");
            if (e) {
                $(this).removeClass(h);
                $(this).addClass(e)
            }
        });
        $("div").each(function () {
            var e = $(this).attr("onTablet");
            var h = $(this).attr("onDesktop");
            if (e) {
                $(this).removeClass(h);
                $(this).addClass(e)
            }
        })
    } else {
        if ($(".main-menu-span").hasClass("span1")) {
            $(".main-menu-span").removeClass("span1");
            $(".main-menu-span").addClass("span2")
        }
        if ($(".brand").hasClass("span1")) {
            $(".brand").removeClass("span1");
            $(".brand").addClass("span2")
        }
        if ($("#content").hasClass("span11")) {
            $("#content").removeClass("span11");
            $("#content").addClass("span10")
        }
        $("a").each(function () {
            if ($(this).hasClass("quick-button span2 changed")) {
                $(this).removeClass("quick-button span2 changed");
                $(this).addClass("quick-button-small span1")
            }
        });
        $(".circleStatsItem, .circleStatsItemBox").each(function () {
            var e = $(this).parent().attr("onTablet");
            var h = $(this).parent().attr("onDesktop");
            if (e) {
                $(this).parent().removeClass(e);
                $(this).parent().addClass(h)
            }
        });
        $(".tempStatBox").each(function () {
            var e = $(this).attr("onTablet");
            var h = $(this).attr("onDesktop");
            if (e) {
                $(this).removeClass(e);
                $(this).addClass(h)
            }
        });
        $("div").each(function () {
            var e = $(this).attr("onTablet");
            var h = $(this).attr("onDesktop");
            if (e) {
                $(this).removeClass(e);
                $(this).addClass(h)
            }
        });
        $(".widget").each(function () {
            var e = $(this).attr("onTablet");
            var h = $(this).attr("onDesktop");
            if (e) {
                $(this).removeClass(e);
                $(this).addClass(h)
            }
        })
    }
    if ($(".timeline")) {
        $(".timeslot").each(function () {
            var e = $(this).find(".task").outerHeight();
            $(this).css("height", e)
        })
    }
};