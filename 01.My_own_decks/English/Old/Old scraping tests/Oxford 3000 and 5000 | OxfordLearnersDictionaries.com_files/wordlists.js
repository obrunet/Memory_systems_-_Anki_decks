/**
 * Wordlist Header Panel
 */
// Display / Hide description
$("#toggleDescription").click(function(){
    $(".wordlistsHiddenContent").toggle(400);
    $("#toggleDescription i").toggleClass('icon-plus2 icon-minus2');
});

var typingTimer;
var doneTypingInterval = 500;
var $input = $('#wordlistsSearch');
var $cross = $('#wordlistsSearch + .cross');
var searchbtn = document.querySelector('input[type="button"]');

searchbtn.addEventListener('click', searchwordlist);

function searchwordlist(){
    clearTimeout(typingTimer);
    typingTimer = setTimeout(doScroll, doneTypingInterval);
}

$input.on('keyup', function(event) {
    clearTimeout(typingTimer);
    if(event.keyCode == 13) {
        typingTimer = setTimeout(doScroll, doneTypingInterval);
    }
});

$input.on('keydown', function() {
    clearTimeout(typingTimer);
});

$input.on('input', function(e){
    if($input.val() == "")
        $cross.css("display", "none");
    else
        $cross.css("display", "inline-block");
});

$cross.on('mousedown', function(){
    document.getElementById("wordlistsSearch").value = "";
});
$cross.on('mouseup', function(){
    $(this).css("display", "none");
});

function doScroll() {
    var searchValue = $input.val().toLowerCase();
    var $elem;
    $("#wordlistsContentPanel li:not(.hidden)").each(function() {
        var headword = $(this).attr("data-hw");
        if (headword >= searchValue) {
            $elem = $(this);
            return false;
        }
    });

    if ($elem) {
        if (isMobile) {
            $elem.get(0).scrollIntoView();
        } else {
            document.getElementById("wordlistsContentPanel").scrollTop = $elem.get(0).offsetTop
                    - document.getElementById("wordlistsContentPanel").offsetTop;
        }
    }
}

/**
 * Wordlist content panel
 */
// Display 'not in dataset' tooltip
$("data > span:first-child").click(function(e) {
    if ($("#wordlistsTooltip").is(":hidden")) {
        $("#wordlistsTooltip").css({'top':e.pageY+15,'left':e.pageX-30});
        $("#wordlistsTooltip").fadeIn(200).delay(2000).fadeOut(400);
    }
});

function applySavedFilters(){
    // Filter on list
    if(savedList == "ox5000Diff"){
        savedList = "ox5000";
        $("#wordlistsContentPanel li[data-ox3000]").addClass("hidden");
    } else if (savedList != "oxford_phrase_list"){
        $("#wordlistsContentPanel li:not([data-"+ savedList +"])").addClass("hidden");
    }

    // Filter on level
    if(jQuery.inArray("ALL", currentSavedLevels) == -1){
        $("#wordlistsContentPanel li:not(.hidden)").each(function(i){
            var level = $(this).attr("data-" + savedList);
            if(jQuery.inArray(level, currentSavedLevels) == -1) {
                $(this).addClass("hidden");
            }
        });
    }

    $("#wordlistsContentPanel").addClass("loaded");
}

applySavedFilters();

/**
 * Wordlist Filter Panel
 */
function closeFilterMenu(){
    $("#wordlistsFilterMenu").removeClass("open");
    //reenable scroll
    $("html").removeClass("disable-scroll");
    $("#wordlistsOverlay").hide();
    $("div[id$=_feedback_minimized]").show();
}
function displayCurrentLevels(){
    var selectedList = $("#filterList").val();
    $(".level-select").hide();
    if(wordlist==="oxford-phrase-list"){
        selectedList = "oxford_phrase_list";
    }
    $("#"+selectedList).show();
}

function getList() {
    if($('#filterList').length)
        return $("#filterList").val();
    else
        return "oxford_phrase_list";
}

$("#wordlistsFilters, #wordlistsBreadcrumb").click(function(){
    $("#wordlistsFilterMenu").addClass("open");
    //disable scroll
    $("html").addClass("disable-scroll");
    $("#wordlistsOverlay").show(); 
    $("div[id$=_feedback_minimized]").hide();
    displayCurrentLevels();
});

$("#closemenu").click(closeFilterMenu);
$("#wordlistsOverlay").click(closeFilterMenu);
$("#filterList").change(displayCurrentLevels);

$("#saveFilters").click(function(){

    // Get Values
    var dataset = $("#filterDataset").val();
    var list = getList();

    // Set Cookies
    document.cookie = 'wl_'+wordlist+'_dataset='+dataset;
    document.cookie = 'wl_'+wordlist+'_list='+list;

    $(".level-select").each(function(){
        var level = [];
        if($(this).find('.ms-select-all input:checked').length) {
            document.cookie = 'wl_'+wordlist+'_'+$(this).attr("id")+'_level=ALL';
        } else {
            $(this).find("input:checked").each(function(){
                level.push($(this).val());
            });
            document.cookie = 'wl_'+wordlist+'_'+$(this).attr("id")+'_level='+ level.join("|");
        }
    });

    // Close the menu
    closeFilterMenu(); 

    // Refresh the content
    window.location = window.location.href.split("?")[0];
});

/**
 * Wordlist Download Panel
 */
function closeDownloadMenu(){
    $("#wordlistsDownloadMenu").removeClass("open");
    //re-enable scroll
    $("html").removeClass("disable-scroll");
    $("#wordlistsOverlay").hide();
    $("div[id$=_feedback_minimized]").show();
}

$("#wordlistsDownload").click(function(){
    $("#wordlistsDownloadMenu").addClass("open");
    //disable scroll
    $("html").addClass("disable-scroll");
    $("#wordlistsOverlay").show();
    $("div[id$=_feedback_minimized]").hide();
});

$("#closeDownloadMenu").click(closeDownloadMenu);
$("#wordlistsOverlay").click(closeDownloadMenu);

$(".ms-parent:visible .not-all input").on("change", function(){
    $(".ms-select-all:visible input").prop('checked', isToggleAll());
})

$(".ms-select-all input").on("change", function(){
    var isChecked = $(this).prop("checked");
    $.each($(".ms-parent:visible .not-all input"), function(){
        $(this).prop("checked", isChecked);
    })
});

function isToggleAll(){
    if($(".ms-parent:visible").find('.not-all input:not(:checked)').length)
        return false;
    return true;
}