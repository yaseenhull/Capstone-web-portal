$(function() {
    /*alert("Starting!");*/
    let selectOriginField = $('#id_citizenship');
    let selectOriginSaField = $('#id_citizenship');
    let selectOtherCountryField = $('#id_country_of_previous_institute');
    let selectOtherDegreeField = $('#id_previous_degree');
    let selectField = $('#id_degree');
    let selectMathField = $('#id_math_level');
    let selectProjectField = $('#id_thesis_completed_previously');
    let forInternational = $('.international-specific');
    let forSA = $('.sa-specific');
    let forOtherCountry = $('.othercountry-specific');
    let forOtherDegree = $('.otherdegree-specific');
    let forMit = $('.mit-specific');
    let forPercentage = $('.math-specific');
    let forProject = $('.project-specific');

    function toggleInternational(value) {
        /*alert("Toggling Mit! val:" + value);*/
        if (value === 'International applicant') {
            forInternational.parent().show();
        } else {
            /*alert("Hiding");*/
            forInternational.parent().hide();
        }

    }

    function toggleSA(value) {
        /*alert("Toggling Mit! val:" + value);*/
        if (value === 'South African citizen' || value === 'South African permanent resident') {
            forSA.parent().show();
        } else {
            /*alert("Hiding");*/
            forSA.parent().hide();
        }

    }

    function toggleOtherCountry(value) {
        /*alert("Toggling Mit! val:" + value);*/
        if (value === 'Other') {
            forOtherCountry.parent().show();
        } else {
            /*alert("Hiding");*/
            forOtherCountry.parent().hide();
        }

    }

    function toggleOtherDegree(value) {
        /*alert("Toggling Mit! val:" + value);*/
        if (value === 'Other') {
            forOtherDegree.parent().show();
        } else {
            /*alert("Hiding");*/
            forOtherDegree.parent().hide();
        }

    }

    function toggleMit(value) {
        /*alert("Toggling Mit! val:" + value);*/
        if (value === 'Masters in Information Technology') {
            forMit.parent().show();
        } else {
            /*alert("Hiding");*/
            forMit.parent().hide();
        }

    }

    function toggleMath(value) {
        /*alert("Toggling Math!");*/
        if (value === '1' || value === '2' || value === '3') {
            forPercentage.parent().show();
        } else {
            forPercentage.parent().hide();
        }
    }

    function toggleProject(value) {
        /*alert("Toggling Project!");*/
        if (value === 'YES') {
            forProject.parent().show();
        } else {
            forProject.parent().hide();
        }
    }

    // show/hide on load based on previous value of selectField
    /*alert("Field Value: " + selectProjectField.val() + "\nField Value: " + selectField.val()
        + "\nField Value: " + selectMathField.val());*/
    toggleInternational(selectOriginField.val());
    toggleSA(selectOriginSaField.val());
    toggleOtherCountry(selectOtherCountryField.val());
    toggleOtherDegree(selectOtherDegreeField.val());
    toggleMit(selectField.val());
    toggleMath(selectMathField.val());
    toggleProject(selectProjectField.val());

    // show/hide on change
    selectOriginField.change(function() {
       /* alert("Select List changed!");*/
        toggleInternational($(this).val());
    });

    selectOriginSaField.change(function() {
       /* alert("Select List changed!");*/
        toggleSA($(this).val());
    });

    selectOtherCountryField.change(function() {
       /* alert("Select List changed!");*/
        toggleOtherCountry($(this).val());
    });

    selectOtherDegreeField.change(function() {
       /* alert("Select List changed!");*/
        toggleOtherDegree($(this).val());
    });

    selectField.change(function() {
       /* alert("Select List changed!");*/
        toggleMit($(this).val());
    });

    selectMathField.change(function() {
        /*alert("Select Math List changed!");*/
        toggleMath($(this).val());
    });

    selectProjectField.change(function() {
        /*alert("Select Project List changed!");*/
        toggleProject($(this).val());
    });

});
